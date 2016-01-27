import pytest
import asyncio
from unittest.mock import MagicMock
import uuid

from gssa.server import GoSmartSimulationServerComponent


known_guid = str(uuid.uuid4())
unknown_guid = str(uuid.uuid4())


def make_coro(result):
    @asyncio.coroutine
    def it():
        return result
    return it


@pytest.fixture(scope="module")
def definition():
    definition = MagicMock()
    definition.guid = known_guid
    return definition


@pytest.fixture(scope="module")
def gsssc(definition):
    server_id = 'test-000000'
    database = MagicMock()
    publish_cb = MagicMock()
    use_observant = False

    gsssc = GoSmartSimulationServerComponent(
        server_id,
        database,
        publish_cb,
        use_observant
    )

    gsssc.current[known_guid] = definition

    return gsssc


# TESTS FROM HERE


@pytest.mark.asyncio
def test_init_succeeds(gsssc):
    result = yield from gsssc.doInit(unknown_guid)
    assert(result is True)


@pytest.mark.asyncio
def test_clean_succeeds(gsssc, definition):
    definition.clean = make_coro(True)

    result = yield from gsssc.doClean(known_guid)

    assert(result is True)


@pytest.mark.asyncio
def test_clean_fails_if_guid_unrecognised(gsssc):
    result = yield from gsssc.doClean(unknown_guid)

    assert(result is False)
