Caameron Nakasone
Sound Class Homework #1
Bart Massey

What I did?
For this assignment I started it off by doing research and figuring out how to implement the code. This involved finding a Goertzel filter equation and figuring out
how to use the filter to decode the message from the sound samples. I used Goertzel filter equation from the embedded.com article (cited in code), I placed the
calculations of the constants in a class. This was I could pass in the target frequency and length to the class and the constants would be calculated for different
frequenies. The actual filter was then placed in its own function to be called with the target frequency calculations class which would then return the magnitude
for the samples. Then following the instructions from the How To of the homework I read in the wav file using scipy.io.wavfile and converted the samples to floats.
On the side I computed how many chunks of samples were going to be needed and created two instances of the filter with target frequencies 2225.0 and 2025.0.
The chunks were then processed through each filter and the bit that resulted was placed in an array. The array was then split into bits of 10, I removed the first
and last bit after verifying them and used a flip method on the array to make big-endian. Finally the array of bytes were then converted to an int, which was then
converted to its corresponding ascii character. The chracters were concatenated together and the message is outputed. 

How it went?
Overall the homework went OK. Without the help of the "How to" and questions asked on slack this assignment would have been much harder to complete. But thanks to
the "How to" it was easier to understand what exactly needed to be done and how to go about doing it. There was still a lot of research that needed to be done on my
part revolving the Goertzel filter equation and how to implement it. This was probably do to my lack of math skills, however reading the embedded article helped 
greatly in understanding it and implementing it. 

After the filter was done the second part of the assignment was not as bad. After figuring out how to exactly obtaint the samples from the wav files, it was just a
matter of doing some math to figure out the correct chunk sizes and manipulating the data to get ascii characters. (Again the "How to" helped out a lot).

What is still to be done?
The requirements for the homework assignment are all done. The filter has been implemented and the wav file was read in parsed into samples and then decoded using
the filter to get a ascii string. There are things such as cleaning up the code more or seperating them in to functions which could be done to make the code
look and perform better. In addition there are the extras part of the homework which have not been done.
