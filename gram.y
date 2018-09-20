%{
  import java.io.*;
  import java.util.ArrayList;
%}
%token WA, MO, DESU, JAARIMASEN, DEWAARIMASEN, DESUKA

%%
sintagmaNominal: substantivo sufixo
			   ;

kei11: sintagmaNominal wamo sintagmaNominal copula
	 | sintagmaNominal wamo sintagmaNominal copula
	 ;
	 
wamo: WA
	| MO
	;
	 
copula: DESU
      | JAARIMASEN
	  | DEWAARIMASEN
	  | DESUKA
	  ;

