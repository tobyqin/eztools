import re

import six


def to_int(input_, default=0, exception=(ValueError, TypeError), regexp=None):
    r'''
    Convert the given input to an integer or return default

    When trying to convert the exceptions given in the exception parameter
    are automatically catched and the default will be returned.

    The regexp parameter allows for a regular expression to find the digits
    in a string.
    When True it will automatically match any digit in the string.
    When a (regexp) object (has a search method) is given, that will be used.
    WHen a string is given, re.compile will be run over it first

    The last group of the regexp will be used as value

    >>> to_int('abc')
    0
    >>> to_int('1')
    1
    >>> to_int('abc123')
    0
    >>> to_int('123abc')
    0
    >>> to_int('abc123', regexp=True)
    123
    >>> to_int('123abc', regexp=True)
    123
    >>> to_int('abc123abc', regexp=True)
    123
    >>> to_int('abc123abc456', regexp=True)
    123
    >>> to_int('abc123', regexp=re.compile(r'(\d+)'))
    123
    >>> to_int('123abc', regexp=re.compile(r'(\d+)'))
    123
    >>> to_int('abc123abc', regexp=re.compile(r'(\d+)'))
    123
    >>> to_int('abc123abc456', regexp=re.compile(r'(\d+)'))
    123
    >>> to_int('abc123', regexp=r'(\d+)')
    123
    >>> to_int('123abc', regexp=r'(\d+)')
    123
    >>> to_int('abc', regexp=r'(\d+)')
    0
    >>> to_int('abc123abc', regexp=r'(\d+)')
    123
    >>> to_int('abc123abc456', regexp=r'(\d+)')
    123
    >>> to_int('1234', default=1)
    1234
    >>> to_int('abc', default=1)
    1
    >>> to_int('abc', regexp=123)
    Traceback (most recent call last):
    ...
    TypeError: unknown argument for regexp parameter: 123
    '''

    if regexp is True:
        regexp = re.compile(r'(\d+)')
    elif isinstance(regexp, six.string_types):
        regexp = re.compile(regexp)
    elif hasattr(regexp, 'search'):
        pass
    elif regexp is not None:
        raise TypeError('unknown argument for regexp parameter: %r' % regexp)

    try:
        if regexp:
            match = regexp.search(input_)
            if match:
                input_ = match.groups()[-1]
        return int(input_)
    except exception:
        return default


def to_float(input_, default=0, exception=(ValueError, TypeError), regexp=None):
    r'''
    Convert the given `input_` to an integer or return default

    When trying to convert the exceptions given in the exception parameter
    are automatically catched and the default will be returned.

    The regexp parameter allows for a regular expression to find the digits
    in a string.
    When True it will automatically match any digit in the string.
    When a (regexp) object (has a search method) is given, that will be used.
    WHen a string is given, re.compile will be run over it first

    The last group of the regexp will be used as value

    >>> '%.2f' % to_float('abc')
    '0.00'
    >>> '%.2f' % to_float('1')
    '1.00'
    >>> '%.2f' % to_float('abc123.456', regexp=True)
    '123.46'
    >>> '%.2f' % to_float('abc123', regexp=True)
    '123.00'
    >>> '%.2f' % to_float('abc0.456', regexp=True)
    '0.46'
    >>> '%.2f' % to_float('abc123.456', regexp=re.compile(r'(\d+\.\d+)'))
    '123.46'
    >>> '%.2f' % to_float('123.456abc', regexp=re.compile(r'(\d+\.\d+)'))
    '123.46'
    >>> '%.2f' % to_float('abc123.46abc', regexp=re.compile(r'(\d+\.\d+)'))
    '123.46'
    >>> '%.2f' % to_float('abc123abc456', regexp=re.compile(r'(\d+(\.\d+|))'))
    '123.00'
    >>> '%.2f' % to_float('abc', regexp=r'(\d+)')
    '0.00'
    >>> '%.2f' % to_float('abc123', regexp=r'(\d+)')
    '123.00'
    >>> '%.2f' % to_float('123abc', regexp=r'(\d+)')
    '123.00'
    >>> '%.2f' % to_float('abc123abc', regexp=r'(\d+)')
    '123.00'
    >>> '%.2f' % to_float('abc123abc456', regexp=r'(\d+)')
    '123.00'
    >>> '%.2f' % to_float('1234', default=1)
    '1234.00'
    >>> '%.2f' % to_float('abc', default=1)
    '1.00'
    >>> '%.2f' % to_float('abc', regexp=123)
    Traceback (most recent call last):
    ...
    TypeError: unknown argument for regexp parameter
    '''

    if regexp is True:
        regexp = re.compile(r'(\d+(\.\d+|))')
    elif isinstance(regexp, six.string_types):
        regexp = re.compile(regexp)
    elif hasattr(regexp, 'search'):
        pass
    elif regexp is not None:
        raise TypeError('unknown argument for regexp parameter')

    try:
        if regexp:
            match = regexp.search(input_)
            if match:
                input_ = match.group(1)
        return float(input_)
    except exception:
        return default


def to_unicode(input_, encoding='utf-8', errors='replace'):
    '''Convert objects to unicode, if needed decodes string with the given
    encoding and errors settings.

    :rtype: unicode

    >>> to_unicode(b'a')
    'a'
    >>> to_unicode('a')
    'a'
    >>> to_unicode(u'a')
    'a'
    >>> class Foo(object): __str__ = lambda s: u'a'
    >>> to_unicode(Foo())
    'a'
    >>> to_unicode(Foo)
    "<class 'eztools.converters.Foo'>"
    '''
    if isinstance(input_, six.binary_type):
        input_ = input_.decode(encoding, errors)
    else:
        input_ = six.text_type(input_)
    return input_


def to_str(input_, encoding='utf-8', errors='replace'):
    '''Convert objects to string, encodes to the given encoding

    :rtype: str

    >>> to_str('a')
    b'a'
    >>> to_str(u'a')
    b'a'
    >>> to_str(b'a')
    b'a'
    >>> class Foo(object): __str__ = lambda s: u'a'
    >>> to_str(Foo())
    'a'
    >>> to_str(Foo)
    "<class 'eztools.converters.Foo'>"
    '''
    if isinstance(input_, six.binary_type):
        pass
    else:
        if not hasattr(input_, 'encode'):
            input_ = six.text_type(input_)

        input_ = input_.encode(encoding, errors)
    return input_


def to_bool(value, default=False, raise_error=False):
    """
       Converts 'something' to boolean. Raises exception for invalid formats
           Possible True  values: 1, True, "1", "TRue", "yes", "y", "t"
           Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
    """
    if str(value).lower() in ("yes", "y", "true", "t", "1"): return True
    if str(value).lower() in ("no", "n", "false", "f", "0", "0.0", "", "none", "[]", "{}", "()"): return False
    if raise_error:
        raise ValueError('Invalid value for boolean conversion: ' + str(value))
    else:
        return default
