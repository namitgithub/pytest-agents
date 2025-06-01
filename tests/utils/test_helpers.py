from app.utils.helpers import get_db

def test_get_db():
    db = get_db()
    assert db is not None  # Ensure that the database mock is not None
    assert hasattr(db, 'query')  # Check if the mock has the query method
    assert hasattr(db, 'execute')  # Check if the mock has the execute method
