test = {
  'name': 'Question virus_detected',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'virus_detected'
          >>> 'virus_detected' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'virus_detected'
          >>> # from its initial state (of ...)
          >>> virus_detected is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(virus_detected)
          16
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(virus_detected) == {'Yes', 'No'}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(virus_detected, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.count_nonzero(virus_detected == 'Yes')
          6
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
