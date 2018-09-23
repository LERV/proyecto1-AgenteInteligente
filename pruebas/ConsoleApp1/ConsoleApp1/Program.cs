using System;  
using System.Speech.Recognition;  

namespace SpeechRecognitionApp  
{  
  class Program  
  {  
    static void Main(string[] args)  
    {  

      // Create an in-process speech recognizer for the en-US locale.  
      using (  
      SpeechRecognitionEngine recognizer =  
        new SpeechRecognitionEngine(  
          new System.Globalization.CultureInfo("en-US")))  
      {

                // Create and load a dictation grammar.  
                //recognizer.LoadGrammar(new DictationGrammar());  
                Choices colors = new Choices();
                colors.Add(new string[] { "Create matrix", "Show route", "Change start position", "Change end position", "Clean" });

                // Create a GrammarBuilder object and append the Choices object.
                GrammarBuilder gb = new GrammarBuilder();
                gb.Append(colors);

                // Create the Grammar instance and load it into the speech recognition engine.
                Grammar g = new Grammar(gb);


                // Create and load a dictation grammar.
                recognizer.LoadGrammar(g);

                // Add a handler for the speech recognized event.  
                recognizer.SpeechRecognized +=   
          new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized);  

        // Configure input to the speech recognizer.  
        recognizer.SetInputToDefaultAudioDevice();  

        // Start asynchronous, continuous speech recognition.  
        recognizer.RecognizeAsync(RecognizeMode.Multiple);  

        // Keep the console window open.  
        while (true)  
        {  
          Console.ReadLine();  
        }  
      }  
    }  

    // Handle the SpeechRecognized event.  
    static void recognizer_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)  
    {  
      Console.WriteLine("Recognized text: " + e.Result.Text);
            if (e.Result.Text.Equals("blue"))
            {
                Console.WriteLine("Fucking shit");
            }
    }  
  }  
}