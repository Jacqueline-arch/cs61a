(define (ascending? asc-lst) 
    (cond
        ((or (null? asc-lst) (null? (cdr asc-lst))) #t)
        (else (and (not(> (car asc-lst) (car(cdr asc-lst)))) (ascending? (cdr asc-lst))))
))


(define (my-filter pred s) 
    (if (null? s)
        '()
        (if (pred (car s))
        (cons (car s) (my-filter pred (cdr s)))
        (my-filter pred (cdr s))
        )
    )
    )

(define (interleave lst1 lst2) 
    (cond
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
    )
    ) 

    

(define (no-repeats lst) 
    (cond
        ((null? lst) `())
        (else (cons (car lst) (no-repeats(filter(lambda (x) (not(= x (car lst)))) (cdr lst)))))
))
