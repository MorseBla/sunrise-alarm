class Layer:
    def update(self, canvas, dt):
        """
        Called every frame.
        - canvas: FrameCanvas from the matrix
        - dt: delta time in seconds since last frame
        Return value: None (draw directly onto canvas)
        """
        raise NotImplementedError

