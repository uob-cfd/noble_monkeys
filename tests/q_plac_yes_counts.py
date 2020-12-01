# See sp_crosstab.py
test = {
  'name': 'Question plac_yes_counts',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'plac_yes_counts'
          >>> 'plac_yes_counts' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'plac_yes_counts'
          >>> # from its initial state (of ...)
          >>> plac_yes_counts is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(plac_yes_counts)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(plac_yes_counts >= 0)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(plac_yes_counts <= 8)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 2.89 < np.mean(plac_yes_counts) < 3.12
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.94 < np.std(plac_yes_counts) < 1.062
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
