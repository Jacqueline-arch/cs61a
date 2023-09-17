(define (substitute s old new) 
    (cond 
      ((null? s) `()) 
      ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
      (else (if (equal? (car s) old) (cons new (substitute (cdr s) old new)) (cons (car s) (substitute (cdr s) old new))))))

; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s)
      nil
      (cons (fn (car s)) (map fn (cdr s)))))

(define (filter fn s)
  (cond 
    ((null? s)    nil)
    ((fn (car s)) (cons (car s) (filter fn (cdr s))))
    (else         (filter fn (cdr s)))))

(define (count x s) 
(cond
      ((null? s) 0)
      ((equal? (car s) x) (+ 1 (count x (cdr s))))
      (else (count x (cdr s)))))

(define (unique s) 
  (cond 
  ((null? s) nil)
  (else (cons (car s) (unique (filter (lambda (x) (not (equal? x (car s)))) (cdr s)))))))
  

(define (tally names)
(cond
  ((null? names) nil)
  (else (append (cons (cons(car names) (cons (count (car names) names) nil)) nil)
               (tally (filter (lambda (x) (not (equal? x (car names)))) (cdr names))))
               )
  
  ))
