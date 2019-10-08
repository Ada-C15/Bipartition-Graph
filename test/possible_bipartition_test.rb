require_relative "test_helper"

describe "possible_bipartition" do
  it "will work for example 1" do
    # Arrange
    dislikes = [ [],
      [2, 3],
      [1, 4],
      [1],
      [2]
    ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    expect(answer).must_equal true
  end

  it "will work for example 2" do
    # Arrange
    dislikes =  [ [],
      [2, 3],
      [1, 3],
      [1, 2]
    ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    expect(answer).must_equal false
  end

  it "will work for example 3" do
    # Arrange
    dislikes = [ [],
      [2, 5],
      [1, 3],
      [2, 4],
      [3, 5],
      [1, 4]
    ]

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    expect(answer).must_equal false
  end

  it "will return true for a graph which can be bipartitioned" do
    # Arrange
    dislikes = [ [3, 6],
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
    expect(answer).must_equal true
  end


  it "will return false for a graph which cannot be bipartitioned" do
    # Arrange
    dislikes = [ [3, 6],
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
    expect(answer).must_equal false
  end

  it "will work for an empty graph" do
    expect(possible_bipartition([])).must_equal true
  end
end