from collections import Counter
from typing import List


class Solution:

  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    # If the hand cannot be evenly divided, impossible
    if len(hand) % groupSize != 0:
      return False

    count = Counter(hand)
    print(count)
    # Sort the unique keys to always start from the smallest card available
    for card in sorted(count):
      if count[card] > 0:
        needed = count[card]
        # Every card from card to card + groupSize - 1 must have at least 'needed' count
        for next_card in range(card, card + groupSize):
          if count[next_card] < needed:
            return False
          count[next_card] -= needed

    return True