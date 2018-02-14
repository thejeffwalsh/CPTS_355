(*Funtion 1: palindrome*)

fun capitalize s = let
  val (x::xs) = explode s
in
  implode (Char.toUpper x :: map Char.toUpper xs)
end;

fun palindromes s =  
  let val cs = explode s in
    cs = rev cs
  end;

fun palindrome s = palindromes(concat (map capitalize (String.tokens (not o Char.isAlpha) s)));

palindrome("aB b ,,,A");
(*Function 2: zip (and reverse)*)

fun aux (accum, [], []) = accum
	| aux (accum, (x::rest), (y::others)) = aux((x,y)::accum,rest,others);

fun reverse [] acc = acc
	|reverse (x::rest) acc = reverse rest (x::acc);
	
fun fix (n, []) = [] | fix (n, x::rest) = if n = 0 then fix(n, rest) else x::fix (n-1, rest);

fun fixWhich (L1, L2) = if List.length(L1) > List.length(L2) then fix (List.length(L2),L1) else fix (List.length(L1), L2);

fun z (L1, L2) = if List.length(L1) > List.length(L2) then aux([], fixWhich(L1, L2), L2) else aux([],L1,fixWhich(L1,L2));

fun zip L1 L2 = let val w = z(L1,L2) in reverse w [] end;



(*Function 3: Find unique values in list*)

fun isolate [] = []
  | isolate (x::xs) = x::isolate(List.filter (fn y => y <> x) xs);

fun uniques(List) = 
if length(isolate(List)) < length(List) 
then false
else true
| uniques([]) = true;

(*Function 4: Find subsets in list*)

fun subsets L =
	let
		fun insert (first, L2) = map (fn x => first::x) L2
		fun subset(L) =
			if (L=[])
				then [nil]
			else
			
subsets(tl(L)) @ insert(hd(L), subsets(tl(L)));
	in
		subset L
	end;

(*Function 5: *)

datatype either = ImAString of string | ImAnInt of int;

datatype eitherTree = LEAF of either | NODE of (eitherTree * eitherTree);

fun eitherSearch (LEAF(ImAnInt x)) y = (x=y)
  | eitherSearch(LEAF(ImAString x)) y = false
  | eitherSearch (NODE (t1,t2)) y = (eitherSearch t1 y)
  orelse (eitherSearch t2 y);

fun eitherTest () =
let
  val L1 = LEAF(ImAnInt 1)
  val L2 = LEAF(ImAnInt 2)
  val L3 = LEAF(ImAnInt 13)
  val L4 = LEAF(ImAnInt 14)
  val L5 = LEAF(ImAnInt 15)
  val L6 = LEAF(ImAString "a")
  val L7 = LEAF(ImAString "b")
  val L8 = LEAF(ImAString "c")
  val L9 = LEAF(ImAString "d")
  val L10 = LEAF(ImAString "e")
  val N1 = NODE (L1,L2)
  val N2 = NODE (N1, L3)
  val N3 = NODE (N2, L4)
  val N4 = NODE (N3, L5)
  val N5 = NODE (N4, L6)
  val N6 = NODE (N5, L7)
  val N7 = NODE (N6, L8)
  val N8 = NODE (N7, L9)
  val N9 = NODE (N8, L10)

    in
      not  (eitherSearch N9 15)
    end;


(*Function 6: treeToString*)
datatype 'a Tree = Empty | LEAF of 'a | NODE of ('a Tree) list;

val L1a = LEAF "a"
val L1b = LEAF "b"
val L1c = LEAF "c"
val L2a = NODE [L1a, L1b, L1c]
val L2b = NODE [L1b, L1c, L1a]
val L3 = NODE [L2a, L2b, L1a, L1b]
val L4 = NODE [L1c, L1b, L3]
val L5 = NODE [L4]
val iL1a = LEAF 1
val iL1b = LEAF 2
val iL1c = LEAF 3
val iL2a = NODE [iL1a, iL1b, iL1c]
val iL2b = NODE [iL1b, iL1c, iL1a]
val iL3 = NODE [iL2a, iL2b, iL1a, iL1b]
val iL4 = NODE [iL1c, iL1b, iL3]
val iL5 = NODE [iL4]

fun treeToString f Node =
let
  fun treeToString2 (Empty) = [""]
    | treeToString2 (NODE([])) = [")"]
    | treeToString2 (LEAF(v)) = [f v]
    | treeToString2 (NODE(x)) = ["("] @ List.concat (map treeToString2 x) @ [")"]
in
  String.concat(treeToString2 Node)
end;

(*use "c:\\Users\\SysAdmin\\Documents\\CPTS_355\\walsh_homework2.sml";*)