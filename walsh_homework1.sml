(*
**Jeff Walsh
**ID#:11409683
**9/13/2017
*)

(*Problem 1: find if the value exists in a list*)
fun exists (e, L) =
	(*If list is empty then it doesn't exist*)
	if null L 
		then false
		(*If e exists at the beginning of list then return true*)
	else if e = hd(L) 
        then true
		(*If it isnt at the beginning of the list then recursive call skipping beginning of the list*)
        else exists (e, tl(L));

(*Problem 2: list the unions for a list*)
(*Note: if I put spacing in this functions, for some reason I get an sml error, very strange*)
(*Description: if a list turns out to be empty, return that one, otherwise call listUnion with x appended to a and use the value y and set that value equal to if a exists in y then the Union between x and y otherwise append a to the value returned with a recursive call of listUnion with x and y*)
fun listUnion ([], L) = L
  | listUnion (L, []) = L
  | listUnion (a::x,y) = if exists(a, y) then listUnion(x,y)
                      else a::listUnion(x,y);				
	
(*Problem 3: list the intersections of a list*)
(*Note: if I put spacing in this functions, for some reason I get an sml error, very strange*)
(*Description: if a list turns out to be empty, return that one, otherwise call listIntersect with x appended to a, and use the value y and set that value equal to if a exists in y then the Union between x and y otherwise append a to the value returned with a recursive call of listUnion with x and y*)
fun listIntersect([],L) = []
 | listIntersect(L,[]) = []
 | listIntersect(a::x,y) =
	if exists(a,y)
		then a::listIntersect(x,y)
    else listIntersect(x,y);
		
(*Problem 4: find the nth element of a list*)
(*Note: if I put spacing in this functions, for some reason I get an sml error, very strange*)
(*Description: if the list is empty return a N/A because there is not a list to check against, set the value of nthElement of L and i if i=1 to the head of the list to get back the correct value, otherwise if the the length of the list is less than your counter break and set to N/A because the value doesn't exist in L otherwise recursive call nthElement with the list, excluding the i, and decrement the iterator*)
fun nthElement([], i) = "N/A"
| nthElement(L, i) = if i = 1 then hd(L)
 else if length L <i then "N/A"
 else nthElement(tl(L), i-1);

(*Problem 5: check the list to see if it's sorted*)
(*Note: if I put spacing in this functions, for some reason I get an sml error, very strange*)
(*Description: If the list is empty then return a true value, because of being vacuously true, otherwise recursive call with a list of lists and set it to true, then recursively call isSorted with x appended to y which is appended to xs and set that value to the boolean value gathered if x is less than equal to y then isSorted with the list y appended to xs, otherwise the boolean received is false*)
fun isSorted([]) = true
| isSorted([L]) = true
| isSorted(x::y::xs) = if x <=y then isSorted(y::xs)   
else false;
		

(*use "c:\\Users\\SysAdmin\\Documents\\Semester 5\\CPTS_355\\walsh_homework1.sml";*)