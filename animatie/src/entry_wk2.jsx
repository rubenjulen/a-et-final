import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { Clip6 } from './Clip6';
import { Clip7 } from './Clip7';
import { Clip8 } from './Clip8';
import t6 from './timing_c6.json';
import t7 from './timing_c7.json';
import t8 from './timing_c8.json';
const FPS = 30;
const Root = () => (<>
  <Composition id="Clip6" component={Clip6} durationInFrames={Math.ceil(t6.total * FPS)} fps={FPS} width={1920} height={1080} />
  <Composition id="Clip7" component={Clip7} durationInFrames={Math.ceil(t7.total * FPS)} fps={FPS} width={1920} height={1080} />
  <Composition id="Clip8" component={Clip8} durationInFrames={Math.ceil(t8.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
