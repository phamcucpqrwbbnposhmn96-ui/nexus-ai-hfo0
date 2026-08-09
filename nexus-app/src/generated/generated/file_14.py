from src.check import check_agent_code

def test_naming_required():
    issues = check_agent_code("def my_agent():\n    pass")
    assert any("命名" in i for i in issues)

def test_security_dangerous():
    issues = check_agent_code("import os\nos.system('rm -rf /')")
    assert any("安全" in i for i in issues)

def test_clean_code():
    issues = check_agent_code("agent_name = 'sample'\npass")
    assert issues == []