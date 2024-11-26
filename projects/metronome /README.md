# Web Metronome

A simple, responsive web-based metronome built with HTML, JavaScript, and Tone.js. This application provides musicians with a reliable tool for tempo practice and rhythm training.

## Features

- **Adjustable Tempo**: Control speed from 40 to 208 BPM using a slider
- **Visual Metronome**: Beat indicator that flashes in sync with the tempo
- **Tap Tempo**: Set the tempo by tapping rhythmically
- **High-Quality Sound**: Clear, pleasant click sound using Tone.js synthesis
- **Responsive Design**: Works on both desktop and mobile devices


## Installation

1. Clone the main repository:
```bash
git clone https://github.com/blazejkapala/micro-projects.git
```

2. Navigate to the metronome project directory:
```bash
cd micro-projects/projects/reflection
```

Alternatively, you can use SVN to checkout only this specific directory:
```bash
svn checkout https://github.com/blazejkapala/micro-projects/trunk/projects/reflection
```

3. No build process is required. Simply open `index.html` in a web browser.

## Dependencies

- [Tone.js](https://tonejs.github.io/) (v14.8.49) - Loaded via CDN

## Usage

1. **Starting/Stopping the Metronome**
   - Click the "Start" button to begin
   - Click "Stop" to pause the metronome
   - The button changes color to indicate the current state

2. **Adjusting Tempo**
   - Use the slider to set tempo between 40-208 BPM
   - Current tempo is displayed above the slider
   - Alternatively, use the "Tap Tempo" button by tapping your desired rhythm

3. **Tap Tempo Feature**
   - Click the "Tap Tempo" button rhythmically
   - The metronome will calculate the average tempo from your last 3 taps
   - Valid tempo range: 40-208 BPM

## Technical Details

### HTML Structure
- Single page application
- Responsive layout using flexbox
- Clean, minimal interface

### JavaScript Features
- Real-time tempo adjustment
- Tap tempo calculation with averaging
- Visual beat indication
- Tone.js synthesis configuration

### Audio Implementation
```javascript
const synth = new Tone.Synth({
  oscillator: {
    type: 'triangle'
  },
  envelope: {
    attack: 0.001,
    decay: 0.1,
    sustain: 0,
    release: 0.1
  }
});
```

## Browser Support

Tested and working in:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Known Limitations

- Requires JavaScript to be enabled
- Audio playback depends on browser audio capabilities
- Performance may vary on older devices

## Future Improvements

Potential features for future versions:
- Different time signatures
- Multiple sound options
- Accent patterns
- Subdivision controls
- Save/load tempo presets
- Keyboard shortcuts

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Tone.js team for the excellent Web Audio framework
- Inspired by traditional mechanical metronomes