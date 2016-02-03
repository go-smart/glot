import pytest
import asyncio.coroutines
import asyncio
from unittest.mock import MagicMock
import uuid
import traceback

from gssa.server import GoSmartSimulationServerComponent


known_guid = str(uuid.uuid4())
unknown_guid = str(uuid.uuid4())


def magic_coro():
    mock = MagicMock()
    return mock, asyncio.coroutine(mock)


@asyncio.coroutine
def wait():
    pending = asyncio.Task.all_tasks()

    relevant_tasks = [t for t in pending if ('test_' not in t._coro.__name__)]
    yield from asyncio.gather(*relevant_tasks)


@pytest.fixture(scope="function")
def definition():
    definition = MagicMock()
    definition.guid = known_guid
    return definition


# We need event_loop as a fixture to ensure it gets
# started before the GSSA setup
@pytest.fixture(scope="function")
def gsssc(definition, event_loop):
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
def test_start_succeeds(gsssc, definition, event_loop):
    # Simulate will get fired off
    simulate, sc = magic_coro()
    gsssc.doSimulate = sc

    # And a handler attached for when its done
    handle_simulation_done, hsdc = magic_coro()
    gsssc._handle_simulation_done = hsdc

    # Run the doStart method
    result = yield from gsssc.doStart(known_guid)

    # Wait until mock simulation done and handled
    yield from wait()

    # Check simulation was correctly called
    simulate.assert_called_with(known_guid)

    # Check mock simulation handler fired when it finished
    args, kwargs = handle_simulation_done.call_args
    handle_simulation_done.assert_called_once_with(args[0], guid=known_guid)

    assert(result is True)


@pytest.mark.asyncio
def test_update_files_succeeds(gsssc, definition):
    files = MagicMock(spec=dict)
    files.items.return_value = (('local', 'remote'),)

    # Run the doUpdateFiles method
    result = yield from gsssc.doUpdateFiles(known_guid, files)

    # Wait until mock simulation done and handled
    yield from wait()

    # Check whether the files were examined exactly once
    files.items.assert_called_once_with()

    # Check the files were passed to the current definition
    definition.update_files.assert_called_with(files)

    assert(result is True)


@pytest.mark.asyncio
def test_request_files_succeeds(gsssc, definition):
    files = MagicMock(spec=dict)
    uploaded_files = MagicMock()
    definition.push_files.return_value = uploaded_files

    # Run the doRequestFiles method
    result = yield from gsssc.doRequestFiles(known_guid, files)

    # Wait until mock simulation done and handled
    yield from wait()

    # Check the files were passed to the current definition
    definition.push_files.assert_called_with(files)

    assert(result is uploaded_files)


@pytest.mark.asyncio
def test_request_files_fails_on_uploaded_error(gsssc, definition):
    files = MagicMock(spec=dict)
    definition.push_files.side_effect = RuntimeError("Upload failure")

    # Run the doRequestFiles method
    result = yield from gsssc.doRequestFiles(known_guid, files)

    # Wait until mock simulation done and handled
    yield from wait()

    # Check the files were passed to the current definition
    definition.push_files.assert_called_with(files)

    assert(result == {})
