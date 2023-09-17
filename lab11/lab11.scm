(define (over-or-under num1 num2) 
       (cond
        ((> num1 num2) 1)
        ((< num1 num2) -1)
        (else 0)))
(define (make-adder num) (lambda (x) (+ x num)))

(define (composed f g) (lambda (x) (f (g x))))

(define (repeat f n)
    (lambda(x)
        (if (> n 0)
            (cond 
            ((= n 1) (f x))
            ((= n 2) ((composed f f) x))
            (else (f ((repeat f (- n 1)) x)))))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
    (if (zero? (modulo (max a b)(min a b)))
    (min a b)
    (gcd (min a b) (modulo (max a b) (min a b)))))




; test
;  (define (nondecreaselist s)

;     (if _____________________________
;         _____________________________
;         (let ((rest _____________________________ ))
;             (if _____________________________
;                 (cons _____________________________ rest)
;                 (cons _____________________________ (cdr rest))
;             )
;         )
;     )
; )

(define (nondecreaselist s)

    (if (equal? s nil)
        `()
        (let ((rest (cdr s) ))
            (if (not(> (car s) (car rest)))
                (cons (car s) (nondecreadList rest))
                (cons (cons (cars) nil) (nondecreaselist(cdr rest)))
        )
    )
)
)
