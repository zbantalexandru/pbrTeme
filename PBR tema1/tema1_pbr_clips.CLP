
(deffacts rule ( inceput))

(defrule intrebare1
(inceput)
=>
(printout t "Ti-ar place sa inveti despre ontologia cuvintelor 
in detrimentul analizei complexe matematice? y1/n1" crlf)
(assert (raspuns (read)))
(retract 1))

(defrule intrebare2.1
(raspuns y1)
=>
(printout t "Stai mai mult cu telefonul in mana in detrimentul 
unui joc bun pe calculator? y2/n2" crlf))
(assert (raspuns (read))

(defrule intrebare2.2
(raspuns n1)
=>
(printout t "Stai mai mult cu telefonul in mana in detrimentul 
unui joc bun pe calculator? y2/n2" crlf))
(assert (raspuns (read))

(defrule intrebare3.1
(raspuns y1)
(raspuns y2)
=>
(printout t "Ti-ar place sa inveti despre ontologia cuvintelor in detrimentul 
statului cu telefonul in mana? y3/n3" crlf))
(assert (raspuns (read))

(defrule intrebare3.2
(raspuns y1)
(raspuns n2)
=>
(printout t "Ti-ar place sa inveti despre ontologia cuvintelor in detrimentul 
unui joc bun pe calculator? y3/n3" crlf))
(assert (raspuns (read))

(defrule intrebare3.3
(raspuns n1)
(raspuns y2)
=>
(printout t "Ti-ar place sa faci analize complexe matematice in detrimentul 
statului cu telefonul in mana? y3/n3" crlf))
(assert (raspuns (read))


(defrule intrebare3.4
(raspuns n1)
(raspuns n2)
=>
(printout t "Ti-ar place sa faci analize complexe matematice in detrimentul
unui joc bun pe calculator? y3/n3" crlf))
(assert (raspuns (read))



(defrule materie1
(raspuns y3)
(raspuns y1)
=>
(printout t "Iti recomand Programare bazată pe reguli" crlf))

(defrule materie2
(raspuns y3)
(raspuns n1)
=>
(printout t "Iti recomand Aspecte computaţionale în teoria numerelor" crlf))

(defrule materie3
(raspuns n3)
(raspuns y2)
=>
(printout t "Iti recomand Tehnici de programare pe platforma Android" crlf))

(defrule materie4
(raspuns n3)
(raspuns n2)
=>
(printout t "Iti recomand Proiectarea jocurilor" crlf))