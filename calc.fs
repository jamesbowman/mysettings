: dec decimal ; : bin 2 base ! ;        \ bases: dec bin hex

: +s begin depth 2/ while + repeat ;    \ sum the stack
: zd. ( d u ) <# 0 ?do # loop #> type ; \ show d, u wide
: z. ( x u ) >r s>d r> zd. ;            \ show x, u wide
: $. '$' emit dup 100 / 0 .r '.' emit abs 2 z. ;

: **2 1 swap lshift ;
: l2 ( x -- y) 0 begin 1+ 2dup **2 < until nip ;
