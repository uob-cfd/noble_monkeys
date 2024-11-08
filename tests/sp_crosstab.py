""" Scipy crosstab, from

https://github.com/scipy/scipy/pull/11352/files

with thanks.
"""
import numpy as np


def crosstab(*args, levels=None):
    """
    Create a table of the counts of the tuples in ``zip(*args)``.
    When ``len(args) > 1``, the array computed by this function is
    often referred to as a *contingency table* [1]_.
    The arguments must be sequences with the same length.  The second return
    value, `count` is an integer array with ``len(args)`` dimensions.  If
    `levels` is None, the shape of `count` is ``(n0, n1, ...)``, where ``nk``
    is the number of unique elements in ``args[k]``.
    Parameters
    ----------
    args : sequences
        A sequence of sequences whose unique aligned elements are to be
        counted.  The sequences in args must all be the same length.
    levels : sequence, optional
        If `levels` is given, it must be a sequence that is the same length as
        `args`.  Each element in `levels` is either a sequence or None.  If it
        is a sequence, it gives the values in the corresponding sequence in
        `args` that are to be counted.  If any value in the sequences in `args`
        does not occur in the corresponding sequence in `levels`, that value
        is ignored and not counted in the returned array `count`.
    Returns
    -------
    elements : tuple of numpy.ndarrays.
        Tuple of length ``len(args)`` containing the arrays of elements that
        are counted in `count`.  These can be interpreted as the labels of
        the corresponding dimensions of `count`.
    count : numpy.ndarray
        Counts of the unique elements in ``zip(*args)``, stored in an array.
        Also known as a *contingency table* when ``len(args) > 1``.
    See Also
    --------
    numpy.unique
    Notes
    -----
    .. versionadded:: 1.5.0
    References
    ----------
    .. [1] "Contingency table", http://en.wikipedia.org/wiki/Contingency_table
    Examples
    --------
    >>> from scipy.stats import crosstab
    Given the lists `a` and `x`, create a contingency table that counts the
    frequencies of the corresponding pairs.
    >>> a = ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B']
    >>> x = ['X', 'X', 'X', 'Y', 'Z', 'Z', 'Y', 'Y', 'Z', 'Z']
    >>> (avals, xvals), count = crosstab(a, x)
    >>> avals.tolist()
    ['A', 'B']
    >>> xvals.tolist()
    ['X', 'Y', 'Z']
    >>> count
    array([[2, 3, 0],
           [1, 0, 4]])
    So `('A', 'X')` occurs twice, `('A', 'Y')` occurs three times, etc.
    Higher dimensional contingency tables can be created.
    >>> p = [0, 0, 0, 0, 1, 1, 1, 0, 0, 1]
    >>> (avals, xvals, pvals), count = crosstab(a, x, p)
    >>> count
    array([[[2, 0],
            [2, 1],
            [0, 0]],
           [[1, 0],
            [0, 0],
            [1, 3]]])
    >>> count.shape
    (2, 3, 2)
    The values to be counted can be set by using the `levels` argument.
    It allows the elements of interest in each input sequence to be
    given explicitly instead finding the unique elements of the sequence.
    For example, suppose one of the arguments is an array containing the
    answers to a survey question, with integer values 1 to 4.  Even if the
    value 1 does not occur in the data, we want an entry for it in the table.
    >>> q1 = [2, 3, 3, 2, 4, 4, 2, 3, 4, 4, 4, 3, 3, 3, 4]  # 1 does not occur.
    >>> q2 = [4, 4, 2, 2, 2, 4, 1, 1, 2, 2, 4, 2, 2, 2, 4]  # 3 does not occur.
    >>> options = [1, 2, 3, 4]
    >>> vals, count = crosstab(q1, q2, levels=(options, options))
    >>> count
    array([[0, 0, 0, 0],
           [1, 1, 0, 1],
           [1, 4, 0, 1],
           [0, 3, 0, 3]])
    If `levels` is given, but an element of `levels` is None, the unique values
    of the corresponding argument are used. For example,
    >>> vals, count = crosstab(q1, q2, levels=(None, options))
    >>> vals
    [array([2, 3, 4]), [1, 2, 3, 4]]
    >>> count
    array([[1, 1, 0, 1],
           [1, 4, 0, 1],
           [0, 3, 0, 3]])
    """
    import numpy as np
    if len(args) == 0:
        raise TypeError("At least one input sequence is required.")

    if not all(len(a) == len(args[0]) for a in args[1:]):
        raise ValueError("All input sequences must have the same length.")

    if levels is None:
        # Call np.unique with return_inverse=True on each argument.
        actual_levels, inverses = zip(*[np.unique(a, return_inverse=True)
                                        for a in args])
        shape = [len(u) for u in actual_levels]
        count = np.zeros(shape, dtype=int)
        np.add.at(count, inverses, 1)
    else:
        # `levels` is not None...
        if len(levels) != len(args):
            raise ValueError('len(levels) must equal the number of input '
                             'sequences')

        args = [np.asarray(arg) for arg in args]
        mask = np.zeros((len(args), len(args[0])), dtype=np.bool_)
        inv = np.zeros((len(args), len(args[0])), dtype=np.intp)
        actual_levels = []
        for k, (levels_list, arg) in enumerate(zip(levels, args)):
            if levels_list is None:
                levels_list, inv[k, :] = np.unique(arg, return_inverse=True)
                mask[k, :] = True
            else:
                q = arg == np.asarray(levels_list).reshape(-1, 1)
                mask[k, :] = np.any(q, axis=0)
                qnz = q.T.nonzero()
                inv[k, qnz[0]] = qnz[1]
            actual_levels.append(levels_list)

        mask_all = mask.all(axis=0)
        shape = [len(u) for u in actual_levels]
        count = np.zeros(shape, dtype=int)
        indices = tuple(inv[:, mask_all])
        np.add.at(count, indices, 1)

    return actual_levels, count

treatment = np.repeat(['HDV', 'PLAC'], [8, 8])
virus_detected = np.repeat(['Yes', 'No'], [6, 10])

n_repeats = 1000
means = np.zeros(n_repeats)
stds = np.zeros(n_repeats)
ps = np.zeros(n_repeats)
for r in range(n_repeats):
    plac_yes_counts = np.zeros(1000)
    for i in np.arange(1000):
        shuffled_virus = np.random.permutation(virus_detected)
        _, shuffled_tab = crosstab(treatment, shuffled_virus)
        plac_yes = shuffled_tab[1, 1]
        plac_yes_counts[i] = plac_yes
    means[r] = np.mean(plac_yes_counts)
    stds[r] = np.std(plac_yes_counts)
    ps[r] = np.count_nonzero(plac_yes_counts >= 6) / 1000

print('Means min / max', np.min(means), np.max(means))
print('Stds min / max', np.min(stds), np.max(stds))
print('ps min / max', np.min(ps), np.max(ps))
