from src.app.main import root


class Test_App:
    def test_read_root(self):
        resp = root()
        
        assert resp == {'apiversion': "1",
           'author': "bvilardi",
           'color': "#9999",
           'head': "default",
           'tail': "default"}