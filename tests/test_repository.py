import asyncio
import pytest

data_ids = {
    "task_1": '1',
    }


@pytest.mark.asyncio(loop_scope="module")
async def test_create(repository):
    task_id = '1'
    owner_id = '1'
    task = {"title": "Test task", "description": "Test description", 'owner_id': owner_id, 'task_id': task_id}
    await repository.create(task)
  
    
    
@pytest.mark.asyncio(loop_scope="module")
async def test_get(repository):
    await asyncio.sleep(0.01)
    result = await repository.get(data_ids['task_1'])
    assert result
    assert result['title'] == 'Test task'


@pytest.mark.asyncio(loop_scope="module")
async def test_get_list(repository):
    result = await repository.get_list()
    assert len(result) == 1


@pytest.mark.asyncio(loop_scope="module")  
async def test_update(repository):
    task = {"title": "Test task", "description": "UPDATED Test description"}
    await repository.update(data_ids['task_1'], owner_id=1, task=task)
    


@pytest.mark.asyncio(loop_scope="module")
async def test_delete(repository):
    await repository.delete(data_ids['task_1'], owner_id=1)
    