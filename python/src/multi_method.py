from itertools import product
from typing import Callable


class Candidate:
    def __repr__(self):
        return f"<{self.__class__.__name__} instance>"


class RelationshipSeeker(Candidate):
    pass


class FriendshipFinder(Candidate):
    pass


class OnlineFriendshipFinder(FriendshipFinder):
    pass


class CasualLooker(Candidate):
    pass


class OnlineCasualLooker(CasualLooker):
    pass


def all_subclasses(cls):
    subclasses = cls.__subclasses__()
    for subclass in cls.__subclasses__():
        # recursively call all subclasses on all the subclasses of cls
        subclasses.extend(all_subclasses(subclass))
    return subclasses


class _MultiMethod:

    def __init__(self, name: str):
        self.name = name
        self.typemap = {}

    def __call__(self, *args):

        args_with_types = sorted(
            zip(args, (arg.__class__ for arg in args)), key=lambda pair: str(pair[1]))
        sorted_types = tuple(ty for _, ty in args_with_types)
        sorted_args = (arg for arg, _ in args_with_types)
        return self.typemap[sorted_types](*sorted_args)

    def register_function_for_types(self, types: tuple[type[Candidate]], function: Callable):
        sorted_types = tuple(sorted(types, key=str))  # sort alphabetically
        types_with_subclasses = []
        for type_argument in sorted_types:
            types_with_subclasses.append(
                [type_argument]+all_subclasses(type_argument))
        for type_tuple in product(*types_with_subclasses):
            print(
                f"Registering {type_tuple} for function {function.__name__}.")
            self.typemap[type_tuple] = function


_multi_registry = {}


def multimethod(*types):

    def register(function: Callable):
        mm = _multi_registry.get(function.__name__)
        if mm is None:
            mm = _multi_registry[function.__name__] = _MultiMethod(
                function.__name__)
        mm.register_function_for_types(types, function)
        return mm

    return register


@multimethod(CasualLooker, FriendshipFinder)
def score(looker: CasualLooker, friendship_finder: FriendshipFinder):
    print(
        f"Scoring CasualLooker ({type(looker)} and FriendshipFinder ({type(friendship_finder)}).")


@multimethod(RelationshipSeeker, FriendshipFinder)
def score(relationship_seeker: RelationshipSeeker, friendship_finder: FriendshipFinder):
    print(f"Scoring RelationshipSeeker and FriendshipFinder.")


score(CasualLooker(), FriendshipFinder())
score(FriendshipFinder(), CasualLooker())
score(RelationshipSeeker(), FriendshipFinder())
score(CasualLooker(), OnlineFriendshipFinder())
score(OnlineCasualLooker(), OnlineFriendshipFinder())
