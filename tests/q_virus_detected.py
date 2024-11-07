test = {
  'name': 'Question virus_detected',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'virus_detected'
          >>> assert 'virus_detected' in vars()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'virus_detected'
          >>> # from its initial state (of ...)
          >>> assert virus_detected is not ...
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert len(virus_detected) == 16
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert set(virus_detected) == {'Yes', 'No'}
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert isinstance(virus_detected, np.ndarray)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert np.count_nonzero(virus_detected == 'Yes') == 6
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
