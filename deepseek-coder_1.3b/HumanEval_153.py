def Strongest_Extension(class_name: str, extensions: list) -> str :  
    strongest = 0     # Initialize the strength of extension as zero initially     
    for ext in reversed(extensions):        // Reversing so that first appearance is highest.         
         cap = sum([1 for c in ext if c.isupper()])  // Check how many uppercase letters there are, then calculate its fractional part    
         sm  = len(ext) -cap   // Calculate the lower cases by subtracting them from total length and add to initialize strength as negative of this sum   
         
        current_strength = cap-sm                
                                  
           if strongest < current_strength:      // Checking for higher strengths, then update it.         else continue   # If the new extension is stronger than previous one just skip and move to next iteration      
               strongest=current_strength              &#34;Update strength of this strongest Extension&#34;  )        return f"{class_name}.{ext}"    }     if __name__ == "__main__":         def test():           print(StrongestExtension('myClass',['AAA','BBB']))       # Call function here to check implementation.            
```     `test() `   This line of code will call the implemented functionalities and provide you with output as per your given requirements which is: my_class'.aaa'     I hope this helps! Please adjust it according to how exactly we need our resultant outputs in real world scenarios or use case.