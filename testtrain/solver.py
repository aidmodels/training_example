from cvpm.solver import Solver

class TestTrainSolver(Solver):
    def __init__(self, toml_file=None):
        super().__init__(toml_file)
        self._enable_train = True
        self.set_ready()
        # set your training hyperparameters
        self._hyperparameters = {
            'step': 10000
        }
    def infer(self, image_file, config):
        return 0

    def train(self, dataPath, hyperparameters, config):
        total_steps = hyperparameters['step']
        import time
        for i in range(total_steps):
            print('training ' + str(i))
            time.sleep(1)
        return True, "success"