# Heartbeat-Classification-Using-Deep-Learning

Heartbeat sounds are generated as blood flows through the valves in the heart. The closing and opening of various valves mark the stages of a blood circulation cycle. Irregularities in the heartbeat, if detected at the right time, can be a crucial factor in treating cardiac disorders and thus prevent them from aggravating and turning fatal.

## Breaking down the heartbeat...
The "beats" in a normal heartbeat consists of two distinct sounds, S1 (Lub) and S2 (Dub). These sounds are generated as the valves in the heart close to facilitate the movement of blood. At the start of each systole, the ventricles squeeze to pump out the blood, shutting the Mitral and the Tricuspid valves and thus producing the 'Lub' sound. Similarly, the 'Dub' sound is produced by the closing of the Aortic and Pulmonic valves, which marks the end of the systole.

**Murmurs** are caused by turbulent blood flow through or near the heart. This can produce audible noise and might be an indicator of an underlying heart problem.

**Extra Heart Sounds**, S3 and S4, are rare and produce a 'gallop' like sound.

**Extrasystole** sounds may appear occasionally and can be identified because there is a heart sound that is out of rhythm involving extra or skipped heartbeats. It doesn't occur periodically, unlike extra heart sounds.

## DataSet used
The data set used has been obtained from Kaggle, here's the link: https://www.kaggle.com/kinguistics/heartbeat-sounds
The data consists of audio recordings from two sources: 
  Set A. from the general public via the iStethoscope Pro iPhone app
  Set B. from a clinic trial in hospitals using the digital stethoscope DigiScope.

The sources have been combined into a single dataset used to train the model. Following are the tags present in the dataset:
1. Normal (subclass of noisy normal present)
2. Murmur (subclass of noisy murmur present)
3. Extra Heart Sound
4. Artifact (noisy recordings with usually no discernable heart sounds)
5. Extrasystole


The attempt is to classify these heartbeats using a Deep Learning Model with LSTM. The concepts, code and model evaluation are included in the python notebook.
