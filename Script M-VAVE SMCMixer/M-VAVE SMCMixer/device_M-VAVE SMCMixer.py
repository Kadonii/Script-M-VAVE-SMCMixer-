# name=SMC_Mixer

import midi
import ui
import sys
import mixer
import transport
import array

            
class MidiControllerConfig():

 def __init__(self):
  self.mixerChannel = 1
  self.mixerBool = 0

 def OnMidiMsg(self, event):


  event.handled = True
  #print(event.handled, event.status, event.data1, event.data2, event.port, event.midiId, event.midiChan, event.midiChanEx)

  # mixerChannel = 1

  if event.midiId == midi.MIDI_NOTEON or midi.MIDI_CONTROLCHANGE:
   if event.pmeFlags & midi.PME_System != 0:
    #print("midi ID:", event.midiId)
   # if event.midiId == midi.MIDI_NOTEON:
    # print(midi.MIDI_NOTEON)



    if event.midiId == midi.MIDI_CONTROLCHANGE:

       # print(midi.MIDI_CONTROLCHANGE) #Midi ID
        print("Midi Value:", event.data2)
        print("Midi Unique ID:", event.data1)
        print("Mixer Channel: ", mixer.trackNumber())
        print(" ")
        
    #Volume in the Mixer

    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data1 == 40: #Fader 1
            mixer.setTrackVolume(self.mixerChannel, (event.data2/127))
        #if event.data1 == 1:
         #   print("Mute 1 Button")
        if event.data1 == 41: # Fader 2
            mixer.setTrackVolume(self.mixerChannel+1, (event.data2/127))
        if event.data1 == 42: # Fader 3
            mixer.setTrackVolume(self.mixerChannel+2, (event.data2/127))
        if event.data1 == 43: # Fader 4
            mixer.setTrackVolume(self.mixerChannel+3, (event.data2/127))
        if event.data1 == 44: # Fader 5
            mixer.setTrackVolume(self.mixerChannel+4, (event.data2/127))
        if event.data1 == 45: # Fader 6
            mixer.setTrackVolume(self.mixerChannel+5, (event.data2/127))
        if event.data1 == 46: # Fader 7
            mixer.setTrackVolume(self.mixerChannel+6, (event.data2/127))
        if event.data1 == 47: # Fader 8
            mixer.setTrackVolume(self.mixerChannel+7, (event.data2/127))

        if event.data1 == 62:
            mixer.setTrackVolume(0, (event.data2/127))


    #Bank Left & Right tryin'

    if event.midiId == midi.MIDI_NOTEON:
        print("notee")
        print("Midi Value:", event.data2)
        print("Midi Unique ID:", event.data1)
        print("Mixer Channel: ", mixer.trackNumber())
        print("Mixer Channel Variable: ",self.mixerChannel)
        print(" ")



        if(event.data1 == 99): # Bank Right
         if(self.mixerChannel != 121):
            self.mixerChannel +=8
            print("Bank Right")
            print("Mixer Channel Variable: ",self.mixerChannel)


        if(event.data1 == 98):
            if(self.mixerChannel >= 9):
             self.mixerChannel -=8
             print("Bank Left")
             

              


    #Panning Mixer
    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data1 == 24: #Pan01
            mixer.setTrackPan(self.mixerChannel, ((event.data2/127)-0.5)/0.501)
        if event.data1 == 25: #Pan02
            mixer.setTrackPan(self.mixerChannel+1, ((event.data2/127)-0.5)/0.501)
        if event.data1 == 26: #Pan03
            mixer.setTrackPan(self.mixerChannel+2, ((event.data2/127)-0.5)/0.501)
        if event.data1 == 27: #Pan04
            mixer.setTrackPan(self.mixerChannel+3, ((event.data2/127)-0.5)/0.501)
        if event.data1 == 28: #Pan05
            mixer.setTrackPan(self.mixerChannel+4, ((event.data2/127)-0.5)/0.501)
        if event.data1 == 29: #Pan06
            mixer.setTrackPan(self.mixerChannel+5, ((event.data2/127)-0.5)/0.501)
        if event.data1 == 30: #Pan07
            mixer.setTrackPan(self.mixerChannel+6, ((event.data2/127)-0.5)/0.501)
        if event.data1 == 31: #Pan01
            mixer.setTrackPan(self.mixerChannel+7, ((event.data2/127)-0.5)/0.501)

    #Buttons
    if event.midiId == midi.MIDI_NOTEON:
        #Mute Buttons
        if event.data1 == 16: #Mute1
#            print("Mute 1 Button")
            mixer.muteTrack(self.mixerChannel)
        if event.data1 == 17: #Mute2
#            print("Mute 2 Button")
            mixer.muteTrack(self.mixerChannel+1)
        if event.data1 == 18: #Mute3
#            print("Mute 3 Button")
            mixer.muteTrack(self.mixerChannel+2)
        if event.data1 == 19: #Mute4
#            print("Mute 4 Button")
            mixer.muteTrack(self.mixerChannel+3)
        if event.data1 == 20: #Mute5
#            print("Mute 5 Button")
            mixer.muteTrack(self.mixerChannel+4)
        if event.data1 == 21: #Mute6
#            print("Mute 6 Button")
            mixer.muteTrack(self.mixerChannel+5)
        if event.data1 == 22: #Mute7
#            print("Mute 7 Button")
            mixer.muteTrack(self.mixerChannel+6)
        if event.data1 == 23: #Mute8
#            print("Mute 8 Button")
            mixer.muteTrack(self.mixerChannel+7)

        #Solo Buttons

        if(event.data1 == 8):
#            print("Solo Button 1")
            mixer.soloTrack(self.mixerChannel)
        if(event.data1 == 9):
#            print("Solo Button 2")
            mixer.soloTrack(self.mixerChannel+1)
        if(event.data1 == 10):
#            print("Solo Button 3")
            mixer.soloTrack(self.mixerChannel+2)
        if(event.data1 == 11):
#            print("Solo Button 4")
            mixer.soloTrack(self.mixerChannel+3)
        if(event.data1 == 12):
#            print("Solo Button 5")
            mixer.soloTrack(self.mixerChannel+4)
        if(event.data1 == 13):
#            print("Solo Button 6")
            mixer.soloTrack(self.mixerChannel+5)
        if(event.data1 == 14):
#            print("Solo Button 7")
            mixer.soloTrack(self.mixerChannel+6)
        if(event.data1 == 15):
#            print("Solo Button 8")
            mixer.soloTrack(self.mixerChannel+7)

        #RecArm Buttons

        if(event.data1 == 0):
#            print("Rec Arm 01")
            mixer.armTrack(self.mixerChannel)
        if(event.data1 == 1):
#            print("Rec Arm 02")
            mixer.armTrack(self.mixerChannel+1)
        if(event.data1 == 2):
#            print("RecArm03")
            mixer.armTrack(self.mixerChannel+2)
        if(event.data1 == 3):
#            print("RecArm04")
            mixer.armTrack(self.mixerChannel+3)
        if(event.data1 == 4):
#            print("Rec Arm 05")
            mixer.armTrack(self.mixerChannel+4)
        if(event.data1 == 5):
#            print("RecArm06")
            mixer.armTrack(self.mixerChannel+5)
        if(event.data1 == 6):
#            print("Rec Arm 07")
            mixer.armTrack(self.mixerChannel+6)
        if(event.data1 == 7):
#            print("Rec Arm 08")
            mixer.armTrack(self.mixerChannel+7)
            
      
        if(event.data1 == 48):
#            print("fx off 1")
            mixer.enableTrackSlots(self.mixerChannel)
        if(event.data1 == 49):
#            print("fx off 2")
            mixer.enableTrackSlots(self.mixerChannel+1)
        if(event.data1 == 50):
#            print("fx off 3")
            mixer.enableTrackSlots(self.mixerChannel+2)
        if(event.data1 == 51):
#            print("fx off 4")
            mixer.enableTrackSlots(self.mixerChannel+3)
        if(event.data1 == 52):
#            print("fx off 5")
            mixer.enableTrackSlots(self.mixerChannel+4)
        if(event.data1 == 53):
#            print("fx off 6")
            mixer.enableTrackSlots(self.mixerChannel+5)
        if(event.data1 == 54):
#            print("fx off 7")
            mixer.enableTrackSlots(self.mixerChannel+6)
        if(event.data1 == 65):
#            print("fx off 8")
            mixer.enableTrackSlots(self.mixerChannel+7)          
            	



# New instance
SMC_Mixer = MidiControllerConfig()

def OnMidiMsg(event):
 SMC_Mixer.OnMidiMsg(event)

#Python is crap, i need ; after a line ._.

