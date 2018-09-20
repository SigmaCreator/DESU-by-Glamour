%%

%byaccj

%{
  private Parser yyparser;

  public Yylex(java.io.Reader r, Parser yyparser) {
    this(r);
    this.yyparser = yyparser;
    yyline = 1;
  }


  public int getLine() {
      return yyline;
  }

%}

%%


は
も
です
で は あり ませ ん
じゃ　あり　ませ　ん

サントス
さん
学生
。



