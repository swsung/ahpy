"This module contains data for tests and demos or such purposes. The data is in (description, matrix, result) tuples"
matrices=[
("'Saaty: How to make a decision', p. 27",

[[1,    3,     5],
[1./3., 1,     3],
[1./5., 1./3., 1]],

[0.64, 0.26, 0.11],

0.037

),
(

"'Saaty: How to make a decision', p. 27, with forced consistency",

[[1,    3,     5    ],
[1./3., 1,     5./3.],
[1./5., 3./5., 1   ]],

[1,1,1]

),
("'Saaty: How to make a decision', p. 34'",

[[1   , 2    , 3    , 4    , 5],
[1./2., 1    , 2    , 3    , 4],
[1./3., 1./2., 1    , 2    , 3],
[1./4., 1./3., 1./2., 1    , 2],
[1./5., 1./4., 1./3., 1./2., 1]],

[0.419, 0.263 , 0.160, 0.097, 0.062],

0.015

),
("'Unknown matrix'",

[[1, 1./7., 1./4., 1./7., 1],
[7,  1,     9,     4,     5],
[4,  1./9., 1,     1./2., 1],
[7,  1./4., 2,     1,     3],
[1,  1./5., 1,     1./3., 1]],

[1,1,1,1,1])
]

		
xmlmodel="""<?xml version = '1.0' encoding = 'iso8859-1' ?>
<model>
	<alternatives>
		<alternative id="1">
			Sybase
			<ratio to="2">0.444</ratio>
			<ratio to="3">1.222</ratio>
		</alternative>
		<alternative id="2">Oracle</alternative>
		<alternative id="3">MySQL</alternative>
	</alternatives>
	<criteria>
		<criterion id="4" name="Price"/>
		<criterion id="5" name="Scalability"/>
	</criteria>
</model>"""

