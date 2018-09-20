%{
  import java.io.*;
  import java.util.ArrayList;
%}
%token WA, MO, NOUN, DESU, JAARIMASEN, DEWAARIMASEN, DESUKA

%%
nominal: NOUN
	   ;

form1: nominal bindingParticle nominal copula
	 ;
	 
bindingParticle: WA
	| MO
	;
	 
copula: DESU
      | JAARIMASEN
	  | DEWAARIMASEN
	  | DESUKA
	  ;

