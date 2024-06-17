#!/usr/bin/env python
# coding: utf-8

# In[49]:
import graphviz
from PySimpleAutomata import automata_IO
from PySimpleAutomata import DFA
import tkinter as tk
from enum import Enum
from tkinter import *
import re
import pandas
import pandastable as pt
from nltk.tree import *
from dfa import DFA



class Token_type(Enum):  # listing all tokens type
    If = 1
    And=2
    Div=3
    File=4
    In = 5
    Of = 6
    Record=7
    Dot = 8
    Semicolon = 9
    EqualOp = 10
    LessThanOp = 11
    GreaterThanOp = 12
    NotEqualOp = 13
    PlusOp = 14
    MinusOp = 15
    MultiplyOp = 16
    DivideOp = 17
    Identifier = 18
    Constant = 19
    Error = 20
    LessThanorEqual = 21
    GreaterThanorEqual = 22
    GreaterLess = 23
    String = 24
    Type=25
    Array=26
    Do = 27
    For=28
    Label=29
    Or=30
    Repeat=31
    Until=32
    Begin=33
    Downto=34
    Function=35
    Mod=36
    Packed=37
    Set=38
    Var=39
    Case=40
    Else=41
    Goto=42
    Nil=43
    Procedure=44
    Then=45
    While=46
    Const=47
    End=48
    Not=49
    Program=50
    To=51
    With=52
    Openpar=53
    Closepar=54
    Assignment=55
    MultiLineComment=56
    NewLine = 57
    Colon = 58
    Readln = 59
    Writeln = 60
    Tab = 61
    SingleLineComment = 62
    Comma = 63
    Integer = 64
    Real = 65
    Char = 66
    StringDT = 67
    Boolean = 68
    Uses = 69
    Library = 70
    Read = 71
    Write = 72
    GreaterThan = 73
    LessThan = 74
# class token to hold string and token type
class token:
    def __init__(self, lex, token_type):
        self.lex = lex
        self.token_type = token_type

    def to_dict(self):
        return {
            'Lex': self.lex,
            'token_type': self.token_type
        }


# Reserved word Dictionary
ReservedWords = {"if": Token_type.If,
                 "and": Token_type.And,
                 "div": Token_type.Div,
                 "file": Token_type.File,
                 "in": Token_type.In,
                 "of": Token_type.Of,
                 "record": Token_type.Record,
                 "type": Token_type.Type,
                 "array": Token_type.Array,
                 "do": Token_type.Do,
                 "for": Token_type.For,
                 "label": Token_type.Label,
                 "or": Token_type.Or,
                 "repeat": Token_type.Repeat,
                 "until": Token_type.Until,
                 "begin": Token_type.Begin,
                 "downto": Token_type.Downto,
                 "function": Token_type.Function,
                 "mod": Token_type.Mod,
                 "packed": Token_type.Packed,
                 "set": Token_type.Set,
                 "var": Token_type.Var,
                 "case": Token_type.Case,
                 "else": Token_type.Else,
                 "goto": Token_type.Goto,
                 "nil": Token_type.Nil,
                 "procedure": Token_type.Procedure,
                 "then": Token_type.Then,
                 "while": Token_type.While,
                 "const": Token_type.Const,
                 "end": Token_type.End,
                 "not": Token_type.Not,
                 "program": Token_type.Program,
                 "to": Token_type.To,
                 "with": Token_type.With,
                 "\n" : Token_type.NewLine,
                 "readln": Token_type.Readln,
                 "writeln": Token_type.Writeln,
                 "\t": Token_type.Tab,
                 "uses" : Token_type.Uses,
                 "library": Token_type.Library,
                 "read": Token_type.Read,
                 "write" : Token_type.Write
                 }
Operators = {".": Token_type.Dot,
             ";": Token_type.Semicolon,
             ":=": Token_type.Assignment,
             "+": Token_type.PlusOp,
             "-": Token_type.MinusOp,
             "*": Token_type.MultiplyOp,
             "/": Token_type.DivideOp,
             "(": Token_type.Openpar,
             ")": Token_type.Closepar,
             ":": Token_type.Colon,
             ",": Token_type.Comma
             }
RelationalOperators = {
             "<=": Token_type.LessThanorEqual,
             ">=": Token_type.GreaterThanorEqual,
             "<>": Token_type.GreaterLess,
             ">": Token_type.GreaterThan,
             "<": Token_type.LessThan,
             "=": Token_type.EqualOp
}
DataTypes = {
            "integer" : Token_type.Integer,
            "real": Token_type.Real,
            "char": Token_type.Char,
            "string": Token_type.StringDT,
            "boolean": Token_type.Boolean
}
Tokens = []  # to add tokens to list
errors = []

def find_token(text):
     #print(text[3])
     j=0
     #print(len(text))
     textlen = len(text)
     while j < len(text):
         #print(len(text))
         #print(j)
        # print(text[j])
         #print(text[j:j+4].lower())
         if(text[j:j+5].lower() == "begin"):

             text = text[:j + 5] + " " + text[j + 5:]
             #print(text)
         if(text[j:j+6].lower() == "repeat"):
             text = text[:j + 6] + " " + text[j + 6:]
         if(text[j:j+5].lower() == "const"):
             text = text[:j + 5] + " " + text[j + 5:]
         if(text[j:j+3].lower() == "var"):
             #text  = text[:j-1] + " " + text[j:]
             text = text[:j+3] + " " + text[j+3:]
         #if (text[j:j + 3].lower() == "end"):
             # text  = text[:j-1] + " " + text[j:]
             #text = text[:j + 3] + " " + text[j + 3:]
         if(text[j:j+4].lower() == "type" ):
             text = text[:j + 4] + " " + text[j + 4:]
         #if (text[j:j + 4].lower() == "begi"):
            # text = text[:j + 4] + " " + text[j + 4:]
         if text[j:j+2].lower() == "do":
             text = text[:j + 2] + " " + text[j + 2:]
        # if (text[j:j + 4].lower() == "uses"):
          #   text = text[:j + 4] + " " + text[j + 4:]
         if (text[j:j + 4].lower() == "then"):
             text = text[:j + 4] + " " + text[j + 4:]
         if(text[j]==';'):
             #print(j)
             #print(text[j])
             text = text[:j+1] + " " + text[j+1:]
            # print(text[:j])



         if(text[j:j+1] == "\n"):
            text = text[:j+1] + " " + text[j+1:]
         if (text[j] == "."):
            text = text[:j+1] + " " + text[j+1:]
         if (text[j] == "}"):
            text = text[:j+1] + " " + text[j+1:]

         if(text[j:j+1] == "\t"):
            text = text[:j+1] + " " + text[j+1:]

         j+=1
     toklist = text.split(" " or "\n")
     #print(multicommentlist)
     # for removing Multiline comments in the tokenized list
     i=0
     # for removing strings in the tokenized list
     while i < len(toklist):
         if toklist[i] in ReservedWords or toklist[i].lower() in ReservedWords:
             Tokens.append(token(toklist[i],ReservedWords[toklist[i].lower()]))
         elif toklist[i] in Operators:
             Tokens.append(token(toklist[i],Operators[toklist[i]]))
         elif toklist[i] in DataTypes:
             Tokens.append(token(toklist[i],DataTypes[toklist[i]]))
         elif toklist[i] in RelationalOperators:
             Tokens.append(token(toklist[i],RelationalOperators[toklist[i]]))
         elif re.match("^[a-zA-Z][a-zA-Z0-9]*$",toklist[i]):
             Tokens.append(token(toklist[i],Token_type.Identifier))
         elif re.match("^[0-9]+(\.[0-9])?$",toklist[i]):
             Tokens.append(token(toklist[i],Token_type.Constant))
         elif re.match("^\'.*$", toklist[i]):  #strings
             if(toklist[i]=="''"):
                 Tokens.append(token("''", Token_type.String))
                 i+=1
                 continue
             combstring = ""
             while re.match("^.*\'$",toklist[i]) is None:
                # print(toklist[i])
                 combstring += toklist[i]
                 combstring+=" "
                 if(i==len(toklist)):break
                 i+=1
             combstring+=toklist[i]
             if(re.match("^.*\'$",toklist[i])):
                 Tokens.append(token(combstring, Token_type.String))
         elif re.match("^{\*.*$", toklist[i]): #Multiline comment
             if (re.match("^{\*.*\*}$", toklist[i])):
                 #Tokens.append(token(toklist[i], Token_type.MultiLineComment))
                 i+=2
                 continue
             combcomm=""
             while re.match("^.*\*}$",toklist[i]) is None:
                 combcomm+=toklist[i]
                 combcomm += " "
                 if (i == len(toklist)): break
                 i+=1
                 combcomm += toklist[i]
             i+=1
             #Tokens.append(token(combcomm, Token_type.MultiLineComment))
         elif re.match("^{.*$",toklist[i]): #single comment
             if re.match("^{.*}$", toklist[i]):
                 #Tokens.append(token(toklist[i], Token_type.SingleLineComment))
                 i += 2
                 continue
             combcomm =""
             flag = False
             while re.match("^.*}$",toklist[i]) is None:
                 if(re.match("^.*\n.*$",toklist[i])):flag=True
                 combcomm += toklist[i]
                 combcomm+= " "
                 if(i == len(toklist)):break
                 i+=1
             combcomm += toklist[i]
             i+=1
             """if flag == False : #Tokens.append(token(combcomm, Token_type.SingleLineComment))
             else : Tokens.append(token(combcomm, Token_type.Error))"""
         else:
             Tokens.append(token(toklist[i],Token_type.Error))
         i+=1
     Tokens.pop(len(Tokens)-1)

def Parse():
    #Header -> program id ;
    j = 0
    Children = []
    Header_dict=Heading(j)
    Children.append(Header_dict["node"])
    uses_out = Uses(Header_dict["index"])
    Children.append(uses_out["node"])
    Decl_out = Declaration(uses_out["index"])
    Children.append(Decl_out["node"])
    exec_out = Execution(Decl_out["index"])
    Children.append(exec_out["node"])
    Node = Tree('Program', Children)
    return Node


def RemoveComm(Tokens):
    for i in Tokens:
        i = i.to_dict()
        if(i["token_type"] == Token_type.SingleLineComment or i["token_type"] == Token_type.MultiLineComment):
            Tokens.pop(Tokens.index(i))

def Execution(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Execution", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    print(Temp["token_type"],j)
    beg_out = Match(Token_type.Begin,j)
    Children.append(beg_out["node"])
    newl_out = Match(Token_type.NewLine,beg_out["index"])
    Children.append(newl_out["node"])
    stats_out = Statements(newl_out["index"])
    Children.append(stats_out["node"])
    end_out = Match(Token_type.End,stats_out["index"])
    Children.append(end_out["node"])
    dot_out = Match(Token_type.Dot,end_out["index"])
    Children.append(dot_out["node"])
    newl2_out = Match(Token_type.NewLine, dot_out["index"])
    Children.append(newl2_out["node"])
    Node = Tree("Execution", Children)
    output["node"] = Node
    output["index"] = newl2_out["index"]
    return output
def Heading(j):
    output = dict()
    Children = []
    p_output = Match(Token_type.Program,j)
    Children.append(p_output["node"])
    id_output = Match(Token_type.Identifier,p_output["index"])
    Children.append(id_output["node"])
    semi_out = Match(Token_type.Semicolon,id_output["index"])
    Children.append(semi_out["node"])
    new_out = Match(Token_type.NewLine,semi_out["index"])
    Children.append(new_out["node"])
    Node = Tree("Header", Children)
    output["node"] = Node
    output["index"] = new_out["index"]
    return output
def Uses(j):
    output = dict()
    Children = []
    Temp = Tokens[j].to_dict()
    #print(Temp["token_type"])
    if Temp["Lex"] == "uses":
        uses_out = Match(Token_type.Uses,j)
        Children.append(uses_out["node"])
        lib_out = Library1(uses_out["index"])
        Children.append(lib_out["node"])
        semi_out = Match(Token_type.Semicolon,lib_out["index"])
        Children.append(semi_out["node"])
        new_out = Match(Token_type.NewLine, semi_out["index"])
        Children.append(new_out["node"])
        Node = Tree("Uses", Children)
        output["node"] = Node
        output["index"] = new_out["index"]
        return output
    else:
        Node = Tree("Uses", Children)
        output["node"] = Node
        output["index"] = j
        return output




def Declaration(j):
    output = dict()
    Children = []
    Temp = Tokens[j].to_dict()
    const_out = Const(j)
    Children.append(const_out["node"])
    type_out = Type(const_out["index"])
    Children.append(type_out["node"])
    var_out = Var(type_out["index"])
    Children.append(var_out["node"])
    func_out = Function(var_out["index"])
    Children.append(func_out["node"])
    proc_out = Procedure(func_out["index"])
    Children.append(proc_out["node"])
    Node = Tree("Declaration",Children)
    output["node"] = Node
    output["index"] = proc_out["index"]
    return output
def Procedure(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Procedure", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    # print(Temp["token_type"],j)
    if (Temp["token_type"] == Token_type.Procedure):
        # print(Temp["token_type"],j)
        func_out = Match(Token_type.Procedure, j)
        Children.append(func_out["node"])
        id_out = Match(Token_type.Identifier, func_out["index"])
        Children.append(id_out["node"])
        semi_out = Match(Token_type.Semicolon, id_out["index"])
        Children.append(semi_out["node"])
        newl_out = Match(Token_type.NewLine, semi_out["index"])
        Children.append(newl_out["node"])
        var_out = Var(newl_out["index"])
        Children.append(var_out["node"])
        # print((Tokens[var_out["index"]].to_dict())["Lex"],var_out["index"])
        # newl2_out = Match(Token_type.NewLine,var_out["index"])
        # Children.append(newl2_out["node"])
        # print(newl2_out["index"],newl2_out["node"])
        beg_out = Match(Token_type.Begin, var_out["index"])
        Children.append(beg_out["node"])
        newli_out = Match(Token_type.NewLine, beg_out["index"])
        Children.append(newli_out["node"])
        Stats_out = Statements(newli_out["index"])
        Children.append(Stats_out["node"])
        #print((Tokens[Stats_out["index"]].to_dict())["Lex"], Stats_out["index"])
        end_out = Match(Token_type.End, Stats_out["index"])
        Children.append(end_out["node"])
        semicol_out = Match(Token_type.Semicolon,end_out["index"])
        Children.append(semicol_out["node"])
        newli2_out = Match(Token_type.NewLine, semicol_out["index"])
        Children.append(newli2_out["node"])
        if newli2_out["index"] >= len(Tokens):
            Node = Tree("Procedure", Children)
            output["node"] = Node
            output["index"] = newli2_out["index"]
            #output = HandleError(Children,newli2_out["index"],"Procedure")
            return output
        Temp = Tokens[newli2_out["index"]].to_dict()
        if Temp["token_type"] == Token_type.Procedure:
            proc2_out = Procedure(newli2_out["index"])
            Children.append(proc2_out["node"])
            Node = Tree("Procedure", Children)
            output["node"] = Node
            output["index"] = proc2_out["index"]
            #output = HandleError(Children, proc2_out["index"], "Procedure")
            return output
        Node = Tree("Procedure", Children)
        output["node"] = Node
        output["index"] = newli2_out["index"]
        #output = HandleError(Children, newli2_out["index"], "Procedure")
        return output
    Node = Tree("Procedure", Children)
    output["node"] = Node
    output["index"] = j
    #output = HandleError(Children, j, "Procedure")
    return output
def Function(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Function", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    #print(Temp["token_type"],j)
    if(Temp["token_type"] == Token_type.Function):
        #print(Temp["token_type"],j)
        func_out = Match(Token_type.Function,j)
        Children.append(func_out["node"])
        id_out = Match(Token_type.Identifier, func_out["index"])
        Children.append(id_out["node"])
        semi_out = Match(Token_type.Semicolon,id_out["index"])
        Children.append(semi_out["node"])
        newl_out = Match(Token_type.NewLine,semi_out["index"])
        Children.append(newl_out["node"])
        var_out = Var(newl_out["index"])
        Children.append(var_out["node"])
        #print((Tokens[var_out["index"]].to_dict())["Lex"],var_out["index"])
        #newl2_out = Match(Token_type.NewLine,var_out["index"])
        #Children.append(newl2_out["node"])
        #print(newl2_out["index"],newl2_out["node"])
        beg_out = Match(Token_type.Begin,var_out["index"])
        Children.append(beg_out["node"])
        newli_out = Match(Token_type.NewLine,beg_out["index"])
        Children.append(newli_out["node"])
        Stats_out = Statements(newli_out["index"])
        Children.append(Stats_out["node"])
        #print((Tokens[Stats_out["index"]].to_dict())["Lex"],Stats_out["index"])
        end_out = Match(Token_type.End,Stats_out["index"])
        Children.append(end_out["node"])
        semicol_out = Match(Token_type.Semicolon, end_out["index"])
        Children.append(semicol_out["node"])
        #print((Tokens[end_out["index"]].to_dict())["Lex"],end_out["index"])
        newli2_out = Match(Token_type.NewLine,semicol_out["index"])
        Children.append(newli2_out["node"])
        #print((Tokens[newli2_out["index"]].to_dict())["Lex"],newli2_out["index"])

        if newli2_out["index"] >= len(Tokens):
            Node = Tree("Function", Children)
            output["node"] = Node
            output["index"] = newli2_out["index"]
            return output
        Temp2 = Tokens[newli2_out["index"]].to_dict()
        if Temp2["token_type"] == Token_type.Function:
            func2_out = Function(newli2_out["index"])
            Children.append(func2_out["node"])
            Node = Tree("Function", Children)
            output["node"] = Node
            output["index"] = func2_out["index"]
            return output
        Node = Tree("Function", Children)
        output["node"] = Node
        output["index"] = newli2_out["index"]
        return output
    Node = Tree("Function", Children)
    output["node"] = Node
    output["index"] = j
    return output



def Library1(j):
    output = dict()
    Children = []
    Temp = Tokens[j].to_dict()
    lib_out = Match(Token_type.Identifier,j)
    Children.append(lib_out["node"])
    lib2_out = Library2(lib_out["index"])
    Children.append(lib2_out["node"])
    Node = Tree("Library1",Children)
    output["node"] = Node
    output["index"] = lib2_out["index"]
    return output
def Library2(j):
    output = dict()
    Children = []
    Temp = Tokens[j].to_dict()
    if Temp["token_type"] == Token_type.Comma:
        comma_out = Match(Token_type.Comma,j)
        Children.append(comma_out["node"])
        lib_out = Match(Token_type.Identifier,comma_out["index"])
        Children.append(lib_out["node"])
        lib2_out = Library2(lib_out["index"])
        Children.append(lib2_out["node"])
        Node = Tree("Library2", Children)
        output["node"] = Node
        output["index"] = lib2_out["index"]
        return output
    Node = Tree("Library2",Children)
    output["node"] = Node
    output["index"] = j
    return output



def Const(j):
    output = dict()
    Children = []
    Temp = Tokens[j].to_dict()
    if Temp["token_type"] == Token_type.Const:
        const_out = Match(Token_type.Const,j)
        Children.append(const_out["node"])
        newl_out = Match(Token_type.NewLine,const_out["index"])
        Children.append(newl_out["node"])
        id_out = Match(Token_type.Identifier,newl_out["index"])
        Children.append(id_out["node"])
        eq_out = Match(Token_type.EqualOp,id_out["index"])
        Children.append(eq_out["node"])
        con_out = Match(Token_type.Constant or Token_type.String,eq_out["index"])
        Children.append(con_out["node"])
        semi_out = Match(Token_type.Semicolon,con_out["index"])
        Children.append(semi_out["node"])
        new_out = Match(Token_type.NewLine,semi_out["index"])
        Children.append(new_out["node"])
        const2_out = Const2(new_out["index"])
        Children.append(const2_out["node"])
        Node = Tree("Const",Children)
        output["node"] = Node
        output["index"] = const2_out["index"]
        return output
    else:
        Node = Tree("Const", Children)
        output["node"] = Node
        output["index"] = j
        return output
def Const2(j):
    output = dict()
    Children = []
    Temp = Tokens[j].to_dict()
    if Temp["token_type"] == Token_type.Identifier:
        id_out = Match(Token_type.Identifier,j)
        Children.append(id_out["node"])
        eq_out = Match(Token_type.EqualOp,id_out["index"])
        Children.append(eq_out["node"])
        val_out = Match(Token_type.Constant,eq_out["index"])
        Children.append(val_out["node"])
        const2_out = Const2(val_out["index"])
        Children.append(const2_out["node"])
        Node = Tree("Const2",Children)
        output["node"] = Node
        output["index"] = const2_out["index"]
        return output
    Node = Tree("Const2", Children)
    output["node"] = Node
    output["index"] = j
    return output
def Type(j):
    output = dict()
    Children = []
    Temp = Tokens[j].to_dict()
    if(Temp["token_type"] == Token_type.Type):
        type_out = Match(Token_type.Type,j)
        Children.append(type_out["node"])
        newl_out = Match(Token_type.NewLine,type_out["index"])
        Children.append(newl_out["node"])
        id_out = Match(Token_type.Identifier,newl_out["index"])
        Children.append(id_out["node"])
        eq_out = Match(Token_type.EqualOp,id_out["index"])
        Children.append(eq_out["node"])
        Temp = Tokens[eq_out["index"]].to_dict()
        #print(Temp["Lex"])
        if(Temp["Lex"] in DataTypes):
            #print("kkkkkkkkkkkkkkkkkkkk")
            dt_out = Match(Temp["token_type"],eq_out["index"])
            Children.append(dt_out["node"])
            semi_out = Match(Token_type.Semicolon,dt_out["index"])
            Children.append(semi_out["node"])
            new_out = Match(Token_type.NewLine,semi_out["index"])
            Children.append(new_out["node"])
            t2_out = Type2(new_out["index"])
            Children.append(t2_out["node"])
            #new_out = Match(Token_type.NewLine,t2_out["index"])
            #Children.append(new_out["node"])
            Node = Tree("Type",Children)
            output["node"] = Node
            output["index"] = t2_out["index"]
            return output
    else:
        Node = Tree("Type", Children)
        output["node"] = Node
        output["index"] = j
        return output


def Type2(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Type2", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    #print(Temp["token_type"])
    if(Temp["token_type"] == Token_type.Identifier):

        id_out = Match(Token_type.Identifier,j)
        Children.append(id_out["node"])
        eq_out = Match(Token_type.EqualOp,id_out["index"])
        Children.append(eq_out["node"])
        Temp2 = Tokens[eq_out["index"]].to_dict()
        if (Temp2["Lex"] in DataTypes):
            dt_out = Match(Temp2["token_type"], eq_out["index"])
            Children.append(dt_out["node"])
            semi_out = Match(Token_type.Semicolon, dt_out["index"])
            Children.append(semi_out["node"])
            newl_out = Match(Token_type.NewLine,semi_out["index"])
            Children.append(newl_out["node"])
            type_out = Type2(newl_out["index"])
            Children.append(type_out["node"])
            Node = Tree("Type2",Children)
            output["node"] = Node
            output["index"] = type_out["index"]
            return output
    Node = Tree("Type2", Children)
    output["node"] = Node
    output["index"] = j
    return output

def Var(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Var", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    #print(Temp["token_type"], "ketfbes",j)
    if(Temp["token_type"] == Token_type.Var):
        var_out = Match(Token_type.Var,j)
        Children.append(var_out["node"])
        n_out = Match(Token_type.NewLine,var_out["index"])
        Children.append(n_out["node"])
        var2_out = Var2(n_out["index"])
        Children.append(var2_out["node"])
        Node = Tree("Var", Children)
        output["node"] = Node
        output["index"] = var2_out["index"]
        return output
    else :
        Node = Tree("Var",Children)
        output["node"] = Node
        output["index"] = j
        return output

def Var2(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Var2", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    if(Temp["token_type"] == Token_type.Identifier):
        id_out = Match(Token_type.Identifier,j)
        Children.append(id_out["node"])
        var_out = Var2(id_out["index"])
        Children.append(var_out["node"])
        Node = Tree("Var2",Children)
        output["node"] = Node
        output["index"] = var_out["index"]
        return output
    elif(Temp["token_type"] == Token_type.Comma):

        comma_out = Match(Token_type.Comma,j)
        Children.append(comma_out["node"])
        id_out = Match(Token_type.Identifier, comma_out["index"])
        Children.append(id_out["node"])
        var_out = Var2(id_out["index"])
        Children.append(var_out["node"])
        Node = Tree("Var2", Children)
        output["node"] = Node
        output["index"] = var_out["index"]
        #print(output["index"])
        return output
    elif(Temp["token_type"] == Token_type.Colon):
        col_out = Match(Token_type.Colon,j)
        Children.append(col_out["node"])
        Temp2 = Tokens[col_out["index"]].to_dict()
        if(Temp2["Lex"] in DataTypes or Temp2["token_type"] == Token_type.Identifier):
            dt_out = Match(Temp2["token_type"],col_out["index"])
            Children.append(dt_out["node"])
            Semi_out = Match(Token_type.Semicolon,dt_out["index"])
            Children.append(Semi_out["node"])
            newl_out = Match(Token_type.NewLine,Semi_out["index"])
            Children.append(newl_out["node"])
            var2_out = Var2(newl_out["index"])
            Children.append(var2_out["node"])
            Node = Tree("Var2",Children)
            output["node"] = Node
            output["index"] = var2_out["index"]
            return output
    else:
        Node = Tree("Var2", Children)
        output["node"] = Node
        output["index"] = j
        return output

















def Statements(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Function", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
   # print(Temp["Lex"],j)
    # newl2_out = Match(Token_type.NewLine,var_out["index"])
    # Children.append(newl2_out["node"])
    # print(newl2_out["index"],newl2_out["node"])
    if (Temp["token_type"] == Token_type.Identifier) or Temp["token_type"] == Token_type.If or Temp["token_type"] == Token_type.Repeat or Temp["token_type"] == Token_type.For or Temp["token_type"] == Token_type.Writeln or Temp["token_type"] == Token_type.Readln or Temp["token_type"] == Token_type.Read or Temp["token_type"] == Token_type.Write  or Temp["token_type"] == Token_type.Constant or Temp["token_type"] == Token_type.While or Temp["token_type"] == Token_type.Error:

        stats_out = Statement(j)
        Children.append(stats_out["node"])
        stats2_out = Statements(stats_out["index"])
        Children.append(stats2_out["node"])
        #print((Tokens[stats_out["index"]].to_dict())["token_type"], stats_out["index"])
        #semi_out = Match(Token_type.Semicolon,stats_out["index"])
        #Children.append(semi_out["node"])
        #print((Tokens[semi_out["index"]].to_dict())["token_type"], semi_out["index"])
        #newl_out = Match(Token_type.NewLine,semi_out["index"])
        #Children.append(newl_out["node"])
        #print((Tokens[newl_out["index"]].to_dict())["token_type"], newl_out["index"])
        Node = Tree("Statements", Children)
        output["node"] = Node
        output["index"] = stats2_out["index"]
        return output
    else:
        Node = Tree("Statements", Children)
        output["node"] = Node
        output["index"] = j
        return output

def Statement(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Statement", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    #print(Temp["token_type"], j)
    if Temp["token_type"] == Token_type.Identifier or Temp["token_type"] == Token_type.Error:
        ass_out = Assign(j)
        Children.append(ass_out["node"])
        Node = Tree("Statement", Children)
        output["node"] = Node
        output["index"] = ass_out["index"]
        return output
    elif Temp["token_type"] == Token_type.If :
        if_out = IFClause(j)
        Children.append(if_out["node"])
        Node = Tree("Statement", Children)
        output["node"] = Node
        output["index"] = if_out["index"]
        return output
    elif Temp["token_type"] == Token_type.For:
        for_out = Match(Token_type.For,j)
        Children.append(for_out["node"])
        id_out = Match(Token_type.Identifier,for_out["index"])
        Children.append(id_out["node"])
        ass_out = Match(Token_type.Assignment,id_out["index"])
        Children.append(ass_out["node"])
        fact_out = Factor(ass_out["index"])
        Children.append(fact_out["node"])
        to_out = Match(Token_type.To,fact_out["index"])
        Children.append(to_out["node"])
        fact2_out = Factor(to_out["index"])
        Children.append(fact2_out["node"])
        do_out = Match(Token_type.Do,fact2_out["index"])
        Children.append(do_out["node"])
        stmt_out = Statement(do_out["index"])
        Children.append(stmt_out["node"])
        Node = Tree("For", Children)
        output["node"] = Node
        output["index"] = stmt_out["index"]
        return output
    elif Temp["token_type"] == Token_type.While:
        while_out = Match(Token_type.While,j)
        Children.append(while_out["node"])
        open_out = Match(Token_type.Openpar,while_out["index"])
        Children.append(open_out["node"])
        cond_out = Condition(open_out["index"])
        Children.append(cond_out["node"])
        close_out = Match(Token_type.Closepar,cond_out["index"])
        Children.append(close_out["node"])
        do_out = Match(Token_type.Do,close_out["index"])
        Children.append(do_out["node"])
        newl_out = Match(Token_type.NewLine,do_out["index"])
        Children.append(newl_out["node"])
        beg_out = Match(Token_type.Begin,newl_out["index"])
        Children.append(beg_out["node"])
        newl2_out = Match(Token_type.NewLine,beg_out["index"])
        Children.append(newl2_out["node"])
        stat_out = Statement(newl2_out["index"])
        Children.append(stat_out["node"])
        end_out = Match(Token_type.End,stat_out["index"])
        Children.append(end_out["node"])
        semi_out = Match(Token_type.Semicolon,end_out["index"])
        Children.append(semi_out["node"])
        newl3_out = Match(Token_type.NewLine,semi_out["index"])
        Children.append(newl3_out["node"])
        Node = Tree("While", Children)
        output["node"] = Node
        output["index"] = newl3_out["index"]
        return output
    elif Temp["token_type"] == Token_type.Repeat:
        rep_out = Match(Token_type.Repeat,j)
        Children.append(rep_out["node"])
        newl2_out = Match(Token_type.NewLine,rep_out["index"])
        Children.append(newl2_out["node"])
        stmt_out = Statements(newl2_out["index"])
        Children.append(stmt_out["node"])
        until_out = Match(Token_type.Until,stmt_out["index"])
        Children.append(until_out["node"])
        cond_out = Condition(until_out["index"])
        Children.append(cond_out["node"])
        semi_out = Match(Token_type.Semicolon,cond_out["index"])
        Children.append(semi_out["node"])
        newl_out = Match(Token_type.NewLine,semi_out["index"])
        Children.append(newl_out["node"])
        Node = Tree("Repeat", Children)
        output["node"] = Node
        output["index"] = newl_out["index"]
        return output
    elif Temp["token_type"] == Token_type.Read:
        read_out = Match(Token_type.Read,j)
        Children.append(read_out["node"])
        left_out = Match(Token_type.Openpar,read_out["index"])
        Children.append(left_out["node"])
        id_out = Match(Token_type.Identifier,left_out["index"])
        Children.append(id_out["node"])
        right_out = Match(Token_type.Closepar,id_out["index"])
        Children.append(right_out["node"])
        semi_out = Match(Token_type.Semicolon,right_out["index"])
        Children.append(semi_out["node"])
        newl_out = Match(Token_type.NewLine,semi_out["index"])
        Children.append(newl_out["node"])
        Node = Tree("Statement", Children)
        output["node"] = Node
        output["index"] = newl_out["index"]
        return output
    elif Temp["token_type"] == Token_type.Readln:
        read_out = Match(Token_type.Readln,j)
        Children.append(read_out["node"])
        left_out = Match(Token_type.Openpar,read_out["index"])
        Children.append(left_out["node"])
        id_out = Match(Token_type.Identifier,left_out["index"])
        Children.append(id_out["node"])
        right_out = Match(Token_type.Closepar,id_out["index"])
        Children.append(right_out["node"])
        semi_out = Match(Token_type.Semicolon, right_out["index"])
        Children.append(semi_out["node"])
        newl_out = Match(Token_type.NewLine, semi_out["index"])
        Children.append(newl_out["node"])
        Node = Tree("Statement", Children)
        output["node"] = Node
        output["index"] = newl_out["index"]
        return output
    elif Temp["token_type"] == Token_type.Writeln:
        writeln_out = WriteLn(j)
        Children.append(writeln_out["node"])
        Node = Tree("WriteLn", Children)
        output["node"] = Node
        output["index"] =writeln_out["index"]
        return output
    elif Temp["token_type"] == Token_type.Write:
        writeln_out = Write(j)
        Children.append(writeln_out["node"])
        Node = Tree("Write", Children)
        output["node"] = Node
        output["index"] = writeln_out["index"]
        return output

    else:
        Node = Tree("Statement", Children)
        output["node"] = Node
        output["index"] = j
        return output

def WriteLn(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("WriteLn", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    writeln_out = Match(Token_type.Writeln,j)
    Children.append(writeln_out["node"])
    open_out = Match(Token_type.Openpar,writeln_out["index"])
    Children.append(open_out["node"])
    Temp = Tokens[open_out["index"]].to_dict()
    if Temp["token_type"] == Token_type.Identifier:
        id_out = Match(Token_type.Identifier,open_out["index"])
        Children.append(id_out["node"])
        writeln2_out = WriteLn2(id_out["index"])
        Children.append(writeln2_out["node"])
        Node = Tree("WriteLn", Children)
        output["node"] = Node
        output["index"] = writeln2_out["index"]
        return output

    id_out = Match(Token_type.String, open_out["index"])
    Children.append(id_out["node"])
    writeln2_out = WriteLn2(id_out["index"])
    Children.append(writeln2_out["node"])
    Node = Tree("WriteLn", Children)
    output["node"] = Node
    output["index"] = writeln2_out["index"]
    return output
def Write(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Write", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    writeln_out = Match(Token_type.Write,j)
    Children.append(writeln_out["node"])
    open_out = Match(Token_type.Openpar,writeln_out["index"])
    Children.append(open_out["node"])
    Temp = Tokens[open_out["index"]].to_dict()
    if Temp["token_type"] == Token_type.Identifier:
        id_out = Match(Token_type.Identifier,open_out["index"])
        Children.append(id_out["node"])
        writeln2_out = Write2(id_out["index"])
        Children.append(writeln2_out["node"])
        Node = Tree("Write", Children)
        output["node"] = Node
        output["index"] = writeln2_out["index"]
        return output

    id_out = Match(Token_type.String, open_out["index"])
    Children.append(id_out["node"])
    writeln2_out = Write2(id_out["index"])
    Children.append(writeln2_out["node"])
    Node = Tree("Write", Children)
    output["node"] = Node
    output["index"] = writeln2_out["index"]
    return output

def Write2(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Write2", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    print(Temp["token_type"], j)

    if Temp["token_type"] == Token_type.Closepar:
        close_out = Match(Token_type.Closepar,j)
        Children.append(close_out["node"])
       # print((Tokens[close_out["index"]].to_dict())["token_type"], close_out["index"])
        semi_out = Match(Token_type.Semicolon,close_out["index"])
        Children.append(semi_out["node"])
       # print((Tokens[semi_out["index"]].to_dict())["token_type"], semi_out["index"])
        newl_out = Match(Token_type.NewLine,semi_out["index"])
        Children.append(newl_out["node"])
        #print((Tokens[newl_out["index"]].to_dict())["token_type"], newl_out["index"])
        Node = Tree("Write2", Children)
        output["node"] = Node
        output["index"] = newl_out["index"]
        return output
    else:
        comma_out = Match(Token_type.Comma,j)
        Children.append(comma_out["node"])
        Temp = Tokens[comma_out["index"]].to_dict()
        #print((Tokens[comma_out["index"]].to_dict())["token_type"], comma_out["index"])

        if Temp["token_type"] == Token_type.Identifier:
            id_out = Match(Token_type.Identifier,comma_out["index"])
            Children.append(id_out["node"])
            writeln2_out = Write2(id_out["index"])
            Children.append(writeln2_out["node"])
            Node = Tree("Write2", Children)
            output["node"] = Node
            output["index"] = writeln2_out["index"]
            return output
        else:
            id_out = Match(Token_type.String, comma_out["index"])
            Children.append(id_out["node"])
            writeln2_out = Write2(id_out["index"])
            Children.append(writeln2_out["node"])
            Node = Tree("Write2", Children)
            output["node"] = Node
            output["index"] = writeln2_out["index"]
            return output
def WriteLn2(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("WriteLn2", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    print(Temp["token_type"], j)

    if Temp["token_type"] == Token_type.Closepar:
        close_out = Match(Token_type.Closepar,j)
        Children.append(close_out["node"])
       # print((Tokens[close_out["index"]].to_dict())["token_type"], close_out["index"])
        semi_out = Match(Token_type.Semicolon,close_out["index"])
        Children.append(semi_out["node"])
       # print((Tokens[semi_out["index"]].to_dict())["token_type"], semi_out["index"])
        newl_out = Match(Token_type.NewLine,semi_out["index"])
        Children.append(newl_out["node"])
        #print((Tokens[newl_out["index"]].to_dict())["token_type"], newl_out["index"])
        Node = Tree("WriteLn2", Children)
        output["node"] = Node
        output["index"] = newl_out["index"]
        return output
    else:
        comma_out = Match(Token_type.Comma,j)
        Children.append(comma_out["node"])
        Temp = Tokens[comma_out["index"]].to_dict()
        #print((Tokens[comma_out["index"]].to_dict())["token_type"], comma_out["index"])

        if Temp["token_type"] == Token_type.Identifier:
            id_out = Match(Token_type.Identifier,comma_out["index"])
            Children.append(id_out["node"])

            writeln2_out = WriteLn2(id_out["index"])
            Children.append(writeln2_out["node"])

            Node = Tree("WriteLn2", Children)
            output["node"] = Node
            output["index"] = writeln2_out["index"]
            return output
        else:
            id_out = Match(Token_type.String, comma_out["index"])
            Children.append(id_out["node"])
            writeln2_out = WriteLn2(id_out["index"])
            Children.append(writeln2_out["node"])
            Node = Tree("WriteLn2", Children)
            output["node"] = Node
            output["index"] = writeln2_out["index"]
            return output
def IFClause(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("IFClause", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    if_out = Match(Token_type.If,j)
    Children.append(if_out["node"])
    open_out = Match(Token_type.Openpar,if_out["index"])
    Children.append(open_out["node"])
    cond_out = Condition(open_out["index"])
    Children.append(cond_out["node"])
    close_out = Match(Token_type.Closepar,cond_out["index"])
    Children.append(close_out["node"])
    then_out = Match(Token_type.Then,close_out["index"])
    Children.append(then_out["node"])
    newll_out = Match(Token_type.NewLine,then_out["index"])
    Children.append(newll_out["node"])
    stmt_out = Statement(newll_out["index"])
    Children.append(stmt_out["node"])
    #print((Tokens[stmt_out["index"]].to_dict())["token_type"], stmt_out["index"])
    Temp = Tokens[stmt_out["index"]].to_dict()
    if Temp["token_type"] == Token_type.Else:
        else_out = Match(Token_type.Else,stmt_out["index"])
        Children.append(else_out["node"])
        stmt2_out = Statement(else_out["index"])
        Children.append(stmt2_out["node"])
        Node = Tree("IFClause", Children)
        output["node"] = Node
        output["index"] = stmt2_out["index"]
        return output
    Node = Tree("IFClause", Children)
    output["node"] = Node
    output["index"] = stmt_out["index"]
    return output

def HandleError(Children,j,str):
    output = dict()
    flag = False
    print(Children[2])
    for i in Children:
        error_out = Match(Token_type.Error,Children.index(i))
        if error_out["node"] == ['error']:
            print("KKKKKKKKKKKKKKKKKKKKK")
            flag = True
    chlength = len(Children)
    if(flag):
        print("KKKKKKKKKKKKKKKKKKKKK2")
        Children.clear()
        Children.append(Token_type.Error)
        Node = Tree("Error",Children)
        output["node"] = Node
        output["index"] = j + chlength
    else:
        Node = Tree(str, Children)
        output["node"] = Node
        output["index"] = j

def Condition(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Condition", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    exp_out = Expression(j)
    Children.append(exp_out["node"])
    Temp = Tokens[exp_out["index"]].to_dict()
    print(Temp["token_type"],j)
    rel_out = Match(RelationalOperators[Temp["Lex"]],exp_out["index"])
    Children.append(rel_out["node"])
    exp2_out = Expression(rel_out["index"])
    Children.append(exp2_out["node"])
    Node = Tree("Condition", Children)
    output["node"] = Node
    output["index"] = exp2_out["index"]
    return output


def Assign(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Assign", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()

    #print(Temp["token_type"],j)
    id_out = Match(Token_type.Identifier,j)
    Children.append(id_out["node"])
    #print((Tokens[id_out["index"]].to_dict())["token_type"],id_out["index"])
    ass_out = Match(Token_type.Assignment,id_out["index"])
    Children.append(ass_out["node"])
    Temp = Tokens[ass_out["index"]].to_dict()
    if Temp["token_type"] == Token_type.String:
        str_out = Match(Token_type.String,ass_out["index"])
        Children.append(str_out["node"])
        semi_out = Match(Token_type.Semicolon, str_out["index"])
        Children.append(semi_out["node"])
        newl_out = Match(Token_type.NewLine, semi_out["index"])
        Children.append(newl_out["node"])
        Node = Tree("Assign", Children)
        output["node"] = Node
        output["index"] = newl_out["index"]
        return output
    #print((Tokens[ass_out["index"]].to_dict())["token_type"], ass_out["index"])
    exp_out = Expression(ass_out["index"])
    Children.append(exp_out["node"])
    #print((Tokens[exp_out["index"]].to_dict())["token_type"], exp_out["index"])
    semi_out = Match(Token_type.Semicolon,exp_out["index"])
    Children.append(semi_out["node"])
    #print((Tokens[semi_out["index"]].to_dict())["token_type"], semi_out["index"])
    newl_out = Match(Token_type.NewLine,semi_out["index"])
    Children.append(newl_out["node"])
    #print((Tokens[newl_out["index"]].to_dict())["token_type"], newl_out["index"])
    Node = Tree("Assign", Children)
    output["node"] = Node
    output["index"] = newl_out["index"]
    return output

def Expression(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Expression", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    term_out = Term(j)
    Children.append(term_out["node"])
    Temp2 = Tokens[term_out["index"]].to_dict()
    if(Temp2["token_type"] == Token_type.PlusOp or Temp2["token_type"] == Token_type.MinusOp):
        add_out = AddOp(term_out["index"])
        Children.append(add_out["node"])
        exp_out = Expression(add_out["index"])
        Children.append(exp_out["node"])
        Node = Tree("Expression", Children)
        output["node"] = Node
        output["index"] = exp_out["index"]
        return output
    else:
        Node = Tree("Expression", Children)
        output["node"] = Node
        output["index"] = term_out["index"]
        return output

def AddOp(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("AddOp", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    if Temp["token_type"] == Token_type.PlusOp:
        plus_out = Match(Token_type.PlusOp,j)
        Children.append(plus_out["node"])
        Node = Tree("AddOp", Children)
        output["node"] = Node
        output["index"] = plus_out["index"]
        return output
    else :
        min_out = Match(Token_type.MinusOp, j)
        Children.append(min_out["node"])
        Node = Tree("AddOp", Children)
        output["node"] = Node
        output["index"] = min_out["index"]
        return output

def Term(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Term", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    factor_out = Factor(j)
    Children.append(factor_out["node"])
    Temp2 = Tokens[factor_out["index"]].to_dict()
    if Temp2["token_type"] == Token_type.MultiplyOp or Temp2["token_type"] == Token_type.DivideOp or Temp2["token_type"] == Token_type.Div or Temp2["token_type"] == Token_type.Mod or Temp2["token_type"] == Token_type.And:
        mult_out = MultOp(factor_out["index"])
        Children.append(mult_out["node"])
        term_out = Term(mult_out["index"])
        Children.append(term_out["node"])
        Node = Tree("Term", Children)
        output["node"] = Node
        output["index"] = term_out["index"]
        return output
    else :
        Node = Tree("Term", Children)
        output["node"] = Node
        output["index"] = factor_out["index"]
        return output

def MultOp(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Function", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    if Temp["token_type"] == Token_type.MultiplyOp or Temp["token_type"] == Token_type.DivideOp:
        sign_out = Match(Operators[Temp["Lex"]] , j)
        Children.append(sign_out["node"])
        Node = Tree("MultOp",Children)
        output["node"] = Node
        output["index"] = sign_out["index"]
        return output
    elif Temp["token_type"] == Token_type.Div:
        div_out = Match(Token_type.Div,j)
        Children.append(div_out["node"])
        Node = Tree("MultOp", Children)
        output["node"] = Node
        output["index"] = div_out["index"]
        return output
    elif Temp["token_type"] == Token_type.Mod:
        mod_out = Match(Token_type.Mod,j)
        Children.append(mod_out["node"])
        Node = Tree("MultOp", Children)
        output["node"] = Node
        output["index"] = mod_out["index"]
        return output
    else:
        and_out = Match(Token_type.And,j)
        Children.append(and_out["node"])
        Node = Tree("MultOp", Children)
        output["node"] = Node
        output["index"] = and_out["index"]
        return output
def Factor(j):
    output = dict()
    Children = []
    if j >= len(Tokens):
        Node = Tree("Function", Children)
        output["node"] = Node
        output["index"] = j
        return output
    Temp = Tokens[j].to_dict()
    if Temp["token_type"] == Token_type.Identifier:
        id_out = Match(Token_type.Identifier,j)
        Children.append(id_out["node"])
        Node = Tree("Factor",Children)
        output["node"] = Node
        output["index"] = id_out["index"]
        return output
    else:
        cons_out = Match(Token_type.Constant, j)
        Children.append(cons_out["node"])
        Node = Tree("Factor", Children)
        output["node"] = Node
        output["index"] = cons_out["index"]
        return output





















def Match(a, j):
    output = dict()
    #Temp = Tokens[j].to_dict()  # in token class to give lexeme and token type a key
    #if Temp["token_type"] == Token_type.SingleLineComment or Temp["token_type"] == Token_type.MultiLineComment:j+=1
    if (j < len(Tokens)):
        Temp = Tokens[j].to_dict() #in token class to give lexeme and token type a key
        if (Temp['token_type'] == a):
            #print(Temp['token_type'], j)
            j += 1
            output["node"] = [Temp['Lex']]
            output["index"] = j
            return output
        elif Temp["token_type"] == Token_type.Error:
            print("ya hoda ya 3antila")
            j+=1
            output["node"] = ["error"]
            output["index"] = j
            return output
        else:
            Temp = Tokens[j].to_dict()
            while Temp["token_type"] != Token_type.NewLine:
                j+=1
                Temp = Tokens[j].to_dict()

            output["node"] = ["error"]
            output["index"] = j
            errors.append("Syntax error : " + Temp['Lex'] + " Expected dot")
            return output
    else:
        Temp = Tokens[j].to_dict()
        while Temp["token_type"] != Token_type.NewLine:
            j += 1
            Temp = Tokens[j].to_dict()
        output["node"] = ["error"]
        output["index"] = j
        return output


# GUI
root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=400, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Scanner Phase')
label1.config(font=('helvetica', 14))
canvas1.create_window(400, 25, window=label1)

label2 = tk.Label(root, text='Source code:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

#entry1 = tk.Entry(root)
#canvas1.create_window(200, 140, window=entry1)
v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')
entry1 = tk.Text(root, width=80, height=15,yscrollcommand=v.set)
#entry1.place(x=120,y=110)
canvas1.create_window(400, 170, window=entry1)
def Scan():
    x1 = entry1.get("1.0",END)
    find_token(x1)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
    print(df)
    dTDa1 = tk.Toplevel()
    dTDa1.title('Token Stream')
    dTDaPT = pt.Table(dTDa1, dataframe=df, showtoolbar=True, showstatusbar=True)
    dTDaPT.show()
    # start Parsing
   # RemoveComm(Tokens)
    Node = Parse()

    # to display errorlist
    df1 = pandas.DataFrame(errors)
    dTDa2 = tk.Toplevel()
    dTDa2.title('Error List')
    dTDaPT2 = pt.Table(dTDa2, dataframe=df1, showtoolbar=True, showstatusbar=True)
    dTDaPT2.show()
    Node.draw()
    # clear your list

    # label3 = tk.Label(root, text='Lexem ' + x1 + ' is:', font=('helvetica', 10))
    # canvas1.create_window(200, 210, window=label3)

    # label4 = tk.Label(root, text="Token_type"+x1, font=('helvetica', 10, 'bold'))
    # canvas1.create_window(200, 230, window=label4)



button1 = tk.Button(text='Scan', command=Scan, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 330, window=button1)

root.mainloop()

# In[ ]: