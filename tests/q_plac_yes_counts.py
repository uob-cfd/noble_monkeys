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
          >>> assert 'plac_yes_counts' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'plac_yes_counts'
          >>> # from its initial state (of ...)
          >>> assert plac_yes_counts is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert len(plac_yes_counts) == 1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.all(plac_yes_counts >= 0)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.all(plac_yes_counts <= 8)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert 2.89 < np.mean(plac_yes_counts) < 3.12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert 0.94 < np.std(plac_yes_counts) < 1.062
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
