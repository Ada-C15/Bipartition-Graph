from graphs.possible_bipartition import possible_bipartition


def test_my_example():
    # Arrange
    dislikes = [[],
                [2],  # 1
                [1],  # 2
                [4],  # 3
                [3],  # 4
                [6],  # 5
                [5, 7],  # 6
                [6, 8],  # 7
                [7, 9],  # 8
                [8]  # 9
                ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert answer


def test_example_1():
    # Arrange
    dislikes = [[],
                [2, 3],
                [1, 4],
                [1],
                [2]
                ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert answer


def test_example_2():
    # Arrange
    dislikes = [[],
                [2, 3],
                [1, 3],
                [1, 2]
                ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer


def test_example_r():
    # Arrange
    dislikes = [[],
                [2, 5],
                [1, 3],
                [2, 4],
                [3, 5],
                [1, 4]
                ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer


def test_will_return_true_for_a_graph_which_can_be_bipartitioned():
    # Arrange
    dislikes = [[3, 6],
                [2, 5],
                [1, 3],
                [0, 2],
                [5],
                [1, 4],
                [0]
                ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert answer


def test_will_return_false_for_graph_which_cannot_be_bipartitioned():
    # Arrange
    dislikes = [[3, 6],
                [2, 5],
                [1, 3],
                [0, 2, 4],
                [3, 5],
                [1, 4],
                [0]
                ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer


def test_will_return_true_for_empty_graph():
    assert possible_bipartition([])


def test_will_return_false_for_another_graph_which_cannot_be_bipartitioned():
    # Arrange
    dislikes = [[3, 6],
                [2, 5],
                [1, 3],
                [0, 2, 4],
                [3, 5],
                [1, 4],
                [0],
                [8],
                [7]
                ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer
