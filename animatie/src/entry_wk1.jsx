import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { KaderA } from './KaderA';
import { Clip5 } from './Clip5';
import tA from './timing_kA.json';
import t5 from './timing_c5.json';

const FPS = 30;
const Root = () => (<>
  <Composition id="KaderA" component={KaderA} durationInFrames={Math.ceil(tA.total * FPS)} fps={FPS} width={1920} height={1080} />
  <Composition id="Clip5" component={Clip5} durationInFrames={Math.ceil(t5.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
