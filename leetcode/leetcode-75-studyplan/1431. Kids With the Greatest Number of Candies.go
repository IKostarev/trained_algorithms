package main

func kidsWithCandies(candies []int, extraCandies int) []bool {
    biggest := 0

    for _, candy := range candies {
      if candy > biggest {
        biggest = candy
      }
    }

    potential := make([]bool, len(candies))

    for i, candy := range candies {
      potential[i] = candy + extraCandies >= biggest
    }
	
    return potential
}