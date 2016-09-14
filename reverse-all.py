# Reverse the reversible rules
# Modified by Alex V to inverse all
# Author: Paul Nasca, 
# based on the invert script by  Andrew Trevorrow

from glife import rect
import golly as g

r = rect( g.getrect() )
if r.empty: g.exit("The pattern is empty.")

for row in xrange(r.top, r.top + r.height):
	for col in xrange(r.left, r.left + r.width):
		cell=g.getcell(col, row)
		if cell==1:
			cell=2
		else:
			if cell==2:
				cell=1
		g.setcell(col, row, cell )



