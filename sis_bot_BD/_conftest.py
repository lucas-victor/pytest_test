from pytest import fixture

@fixture(scope="module")
def fixture_testplan():
    return TestPlan(PLANO_DE_TESTE).get_plano_teste