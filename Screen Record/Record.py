

def record():

    from pynput import mouse
    from pynput import keyboard
    import time

    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        #if not pressed:
            # Stop listener
           # return False


    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:

            # Stop listeners
            m_listener.stop()
            #time.sleep(2)
            #k_listener.stop()

    # Collect events until released
    with keyboard.Listener(on_release=on_release) as k_listener, \
            mouse.Listener(on_click=on_click) as m_listener:
        k_listener.join()
        m_listener.join()

