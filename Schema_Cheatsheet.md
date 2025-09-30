**Understanding the schema**

| CHEAT CODES \- in the schema, the punctuation marks matter. Here’s how: *Combination Indicators:* , (comma) \= elements must appear in an exact, particular order | (pipe)      \= indicates a choice, you can pick one or the other (more on this below) *Repetition Indicators* (number of times an element can or must be used) ? (question mark) \= 0 or 1 (not required, but can only be used once) \+ (plus sign)         \= 1 or more (MUST be one, can be more) \* (asterisk)            \= 0 or more (not required, can be used multiple times) Blank (meaning an element or attribute name with no mark after it) \= must appear 1 time  |
| :---- |

| COLOR CHEAT CODES \- in the schema, the colors of the words tell us something about the meaning of the words |  |
| :---- | :---- |
| Blue \= elements, which generally allow us to insert text inside the carats, like |  |
| name \= element name {...} | \<name\>Mothra\</name\>  |
| Orange \= attributes, which are listed inside the parent element tag, like |  |
| sex \= attribute sex {...} | \<name sex \= “unk\>Godzilla\</name\> |
| Red \= potential responses in elements or attributes |  |
| sex \= attribute sex {“m”, “f”, “unk”} | \<name sex \= “unk\>Godzilla\</name\> |
| Green \= Comments, info about the tags to help us understand how to use them |  |
|  |  |
| Put them all together and you get | \<name sex \= “unk”\>Godzilla\</name\> \#fun |

SYNTAX of SCHEMA

**I) Syntax**  
The schema is meant to control for what elements you can use, what attributes you can use, and where you can use them in your .xml document.  To do so, it defines name of element and attributes using the following format:

data \= element data {...}   
metadata \= attribute metadata {...}

The names *inside* the {...} curvy brackets represent the elements and attributes that *can* or *must* be nested within the elements being named in that line.

data \= element data {metadata} 

* This example names an element “data” and says that another element or attribute named “metadata” will be nested within the “data” element.  
* To know if the name refers to an element or attribute, you will have to find where it is defined in the schema.  Generally, the definitions are in order, but in some instances where an attribute or element is used multiple times throughout the schema, they may appear somewhere else.   
* If “metadata” is an element, the code in XML would look like this \-

			\<data\>  
				\<metadata\>...\</metadata\>  
			\</data\>

* If “metadata” is an attribute, the code in XML would like like this \-

   \<data metadata\=”...”\> \</data\>

1. The quotation marks are required (and you can use single or double marks, but you have to use the same to open and close the attribute in question)  
2. The information in the attribute will appear in red in your .xml document in Oxygen

**II) Spelling**  
The names have to be spelled exactly the same way as in the schema, including case, or Oxygen will not recognize them and will mark an error.

**III) Attribute syntax**  
In some instances the potential format and/or content of an attribute can be controlled by the schema.  

For example, see:   
proctor \= element proctor {sucks} \# this names the element  
sucks \= attribute sucks {“y” | “n”} \# this names the attribute

The code in XML would look like-  
	\<proctor sucks \= “y”\>\</proctor\>  or \<proctor sucks\=”n”\>\</proctor\>

Oxygen would flag the following because the response was NOT defined in the schema  
	\<proctor sucks \= “maybe”\>\</proctor\> 

**IV) Data within element tags \- “text” and “mixed”**  
The schema controls the type of information that you can include *between* the element tags. If the schema does not specify what can be placed in between the open and close tags for an element, you will not be able to add data there

1) “text” \- If an element or attribute definition includes the word “text”, then you will be able to include text between the element tags or in the attribute.  See the following \- 

   proctor \= element proctor {sucks, text} \# names the element says “ text” ok here

   sucks \= attribute sucks {“y” | “n”} \# this names the attribute

   

   The code in XML would look like-

   	\<proctor sucks \= “y”\>he really sucks\!\</proctor\> 

   

2) “Mixed” \- if an element definition includes the word “mixed”, the program allows for a mixture of text and element tags. If it does not say mixed, it will prevent the inclusion of a mixture of text and element tags. See the following \-  
   	proctor \= element proctor {mixed{sucks, name}} \# names the element   
   	name \= element name {text}  
   sucks \= attribute sucks {“y” | “n”} \# this names the attribute  
     
   The XML code would look like:  
   	\<proctor sucks=”y”\> That lame-o \<name\>Proctor\</name\> is really lame\</proctor\>  
   

NOTE \- If you are unsure about what an element tag might mean, I have added a brief comment to explain what they are and should be used for  
