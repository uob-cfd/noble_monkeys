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
          >>> 'p_ge_observed' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_ge_observed'
          >>> # from its initial state (of ...)
          >>> p_ge_observed is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 <= p_ge_observed <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p_ge_observed <= 0.01
          True
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
