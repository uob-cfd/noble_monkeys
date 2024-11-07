# See sp_crosstab.py
test = {
  'name': 'Question p_ge_observed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_ge_observed'
          >>> assert 'p_ge_observed' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_ge_observed'
          >>> # from its initial state (of ...)
          >>> assert p_ge_observed is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert 0 <= p_ge_observed <= 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert p_ge_observed <= 0.01
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
