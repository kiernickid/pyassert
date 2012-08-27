from .matcher_registry import Matcher, register_matcher

__author__ = "Alexander Metzner"

class BaseMatcher (Matcher):
    "Base class for matchers that have a single expected value."
    def __init__ (self, expected):
        self._expected = expected


@register_matcher("equals")
class EqualsMatcher (BaseMatcher):
    "Matcher that tests whether two object are equal, i.e. actual == expected"
    def matches (self, actual):
        return self._expected == actual 

    def describe (self, actual):
        return "Actual '%s' does not equal expected '%s'" % (actual, 
                                                             self._expected)


@register_matcher("is_identical_to")
class IsMatcher (BaseMatcher):
    "Matcher that tests whether two objects are identical, i.e. actual is expected"
    def matches (self, actual):
        return self._expected is actual

    def describe (self, actual):
        return "'%s' is not '%s'" % (actual, self._expected)

@register_matcher("is_a")
class IsTypeMatcher (BaseMatcher):
    """
    Matcher that tests whether the actual value is of a given type.
    
    Examples
    
    assert_that(7).is_a(int)
    assert_that(7.2).is_a(float)
    """
    
    def matches (self, actual):
        return self._expected is actual.__class__
    
    def describe (self, actual):
        return "'%s' of type %s is not of expected type %s" % (actual, 
                                                               actual.__class__,
                                                               self._expected)