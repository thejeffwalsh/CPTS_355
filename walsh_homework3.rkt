#lang racket
;Problem 1: flatten
(define (flatten xss)
  (match xss
    [(list) (list)]
    [(? (compose not list?)) (list xss)]
    [(list x xs ...) (append (flatten x) (flatten xs))]))

;test cases
(flatten '(1 (2 (3 4(5 6)7(8(9(10)11)))))) '(1 2 3 4 5 6 7 8 9 10 11)
(flatten '((1)(2 (2)) (3(3(3))) (4(4(4(4)))))) '(1 2 2 3 3 3 4 4 4 4)
(flatten '( () ))

;Problem 2: replace
(define(replace n v L)
  (list-set L n v))
;test cases
(replace 3 40 '(1 2 3 4 (5) "6"))'(1 2 3 40 (5) "6")
(replace 4 5 '(1 2 3 4 (5) "6")) '(1 2 3 4 5 "6")
(replace 0 9 '("6" 10 11 12 )) '(9 10 11 12)


;Problem 3: mergeUnique2
(define (mergeUnique2 lst1 lst2) 
  (cond ((null? lst1) lst2)    ; if the first list is empty, return the second
        ((null? lst2) lst1)    ; if the second list is empty, return the first
        (else (cons (car lst1) ; otherwise `cons` the first element of the first list
                    (remove-duplicates(mergeUnique2 lst2 (cdr lst1)))))))


;Problem 4: mergeUniqueN
(define (fold mergeUnique2 base L)
(cond
  [(null? L) base]
  [else (fold mergeUnique2 (mergeUnique2 base (car L)) (cdr L))]))

;test case
(fold mergeUnique2 '() '((2 4 6) (1 4 5 6))) ;returns '(1 2 4 5 6)
;helper function to print the test result
(define (bool2str val) (if val "true" "false"))
;define the test function
(define (testMergeUnique)
(let* ([T1 (equal? (mergeUnique2 '(4 6 7) '(3 5 7)) '(3 4 5 6 7) )]
 [T2 (equal? (mergeUnique2 '(1 5 7) '(2 5 7)) '(1 2 5 7) )]
 [T3 (equal? (mergeUnique2 '() '(3 5 7)) '(3 5 7) )] )
 (display(string-append "\n-------\n mergeUnique2 \n T1: " (bool2str T1)
 ", T2: " (bool2str T2)
 ", T3: " (bool2str T3)))))
;call the test function
(testMergeUnique)

;Problem 5: unzip
(define (unzip lst)
  (match lst
    ['() (values '() '())]
    [(cons (list a b) tl)
     (define-values (as bs) (unzip tl))
     (values (cons a as) (cons b bs))]))
;Tests
(unzip '((1 “a”) (5 “b”) (8 “c”)))
(unzip '((1 2) (3 4) (5 6)))

;Peoblem 6: numberToSum
(define (numbersToSum sum L)
  (cond [(null? L) '()]
        [(eq? (- sum (car L)) 0) '()]
        [(< (- sum (car L)) 0) '()]
        [else (cons (car L) (numbersToSum (- sum (car L)) (cdr L)))]))

;obsoleted function
;(define (removeLast L) (reverse (cdr (reverse L))))

;obsolete version
;(define (numbersToSum sum L) (removeLast (numCheck sum L)))

;test cases
(numbersToSum 100 '(10 20 30 40))
(numbersToSum 30 '(5 4 6 10 4 2 1 5))
(numbersToSum 5 '(5 4 6))

;Problem 7: Streams
;a Square Stream
(define squares
  (letrec ([f (lambda (x) (cons (if (= (remainder x 1) 0) (* x x) x)
                                (lambda () (f (+ x 1)))))])
    (lambda () (f 1))))

(define (num-until1 stream n)
(if (<= n (car (stream)))
'()
(cons (car (stream)) (num-until1 (cdr (stream)) n))))

(num-until1 squares 100)

;b streamSum
(define (streamSum sum stream)
  (let ([pr (stream)])
  (cond [(null? pr) '()]
        [(eq? (- sum (car pr)) 0) '()]
        [(< (- sum (car pr)) 0) '()]
        [else (cons (car pr) (streamSum (- sum (car pr)) (cdr pr)))])))

;obsoleted version
;(define (streamSum sum S) (removeLast (numCheck sum S)))

;test cases
(streamSum 10000 squares)
(streamSum 99999999999 squares) 
(streamSum 999999 squares)



