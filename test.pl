towers([ ], A, B, C) => [ ].
towers([ D | L ], A, B, C ) =>
  append( towers(L, A, C, B), [move(D,A,B) | towers(L, C, B, A)] ).
