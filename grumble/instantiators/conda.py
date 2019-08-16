from .interface import EnvironmentProviderInterface

from conda.api import Solver, TransactionHandler
import copy


class CondaEnvironmentProvider(EnvironmentProviderInterface):
    def __init__(self, environment_model):
        self.envionrment_model = environment_model

    def install(self, prefix):
        specs = [pkg.to_matchspec() for pkg in self.envionrment_model.conda_packages]
        import ipdb; ipdb.set_trace()

        solver = Solver(
            prefix, self.envionrment_model.config.channels,
            subdirs=self.envionrment_model.config.subdirs, specs_to_add=specs
        )
        unlink_link_transaction = solver.solve_for_transaction()
        TransactionHandler(unlink_link_transaction).execute(prefix, self.envionrment_model.conda_packages, True)

    def freeze(self, subdir=None):
        new_obj = copy.deepcopy(self.__dict__)
        # solve for specs with given info
        new_obj['packages'] = conda.api.solve()
        new_obj['frozen'] = True
        return CondaEnvironmentProvider(**new_obj)

    def post_apply_steps(self):
        raise NotImplementedError

    def merge(self, other):
        """Inheritance.

        Keys from other are inherited.
            * Any list values are extended, with the list from other appended to the list from self
            * Any string or numeric key from other is clobbered by the same key from self

        Only one level is allowed, but you can stack arbitrarily."""
        merged = copy.deepcopy(self.__dict__())
        for k, v in other.__dict__():
            if k in merged and getattr(self, k):
                if isinstance(v, (string_types, bool)):
                    pass
                else:
                    list_of_stuff = merged.get(k, [])
                    for entry in v:
                        if entry not in list_of_stuff:
                            list_of_stuff.append(entry)
                    merged[k] = list_of_stuff
            else:
                merged[k] = v
        return CondaEnvironmentProvider(**merged)

    def env_vars(self):
        pass
