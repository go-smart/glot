import pytest
import asyncio
from unittest.mock import MagicMock
import uuid

from gssa.server import GoSmartSimulationServerComponent


known_guid = str(uuid.uuid4())
unknown_guid = str(uuid.uuid4())


@pytest.fixture(scope="function")
def definition():
    definition = MagicMock()
    definition.guid = known_guid
    return definition


@pytest.fixture(scope="function")
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
    definition.clean = asyncio.coroutine(lambda: True)

    result = yield from gsssc.doClean(known_guid)

    assert(result is True)


@pytest.mark.asyncio
def test_clean_fails_if_guid_unrecognised(gsssc):
    result = yield from gsssc.doClean(unknown_guid)

    assert(result is False)


@pytest.mark.asyncio
def test_start_succeeds(gsssc, definition):
    simulate = MagicMock()
    gsssc.doSimulate = asyncio.coroutine(simulate)
    simulate.assert_called_with(known_guid)
    gsssc._handle_simulation_done = MagicMock().assert_called_once()

    result = yield from gsssc.doStart(known_guid)

    assert(result is True)
