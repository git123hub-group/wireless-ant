Wireless Ants World (A.Yu.Vlasov)

Reversible cellular automaton with four states based on irreversible CA with two states.
---------------------------------------------------------------------------------------
 
Rule WlAnt:

There are four states: 0 (empty, white), 1 (red), 2 (green), 3 (blue).

A cell with state 0 or 2 (white or green) is called "even"
and a cell with state 1 or 3 (red or blue) is called "odd"

A step may be divided into two stages:

First stage: 
Mark all cells satisfying two conditions: 
(1) total number of odd cells in four closest positions (up, down, left, right) is one or two,  
(2) cells in four diagonal positions are even.

Second stage: 
For unmarked: exchange red and green cells (1<->2). 
For marked cells: change empty into red, red into blue, blue into green, 
green into empty (0->1->3->2->0).

---------------------------------------------------------------------------------------

Three modifications of the WlAnt rule have differences only in condition (1) in the first stage

WlAnt-2 - total number of odd cells in closest positions is any nonzero number (1,2,3,4)

WlAnt-3 - total number of odd cells in closest positions is one, two or three

WlAnt-4 - total number of odd cells in closest positions is either one 
          or two in _opposite_ positions (i.e. up/down or left/right)
---------------------------------------------------------------------------------------

Note:
Script reverse-all.py exchanges all red and green cells to reverse evolution of such automata