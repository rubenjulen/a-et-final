import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { Clip9 } from './Clip9';
import { Clip10 } from './Clip10';
import { KaderB } from './KaderB';
import t9 from './timing_c9.json';
import t10 from './timing_c10.json';
import tB from './timing_kB.json';

const FPS = 30;
const Root = () => (<>
  <Composition id="Clip9" component={Clip9} durationInFrames={Math.ceil(t9.total * FPS)} fps={FPS} width={1920} height={1080} />
  <Composition id="Clip10" component={Clip10} durationInFrames={Math.ceil(t10.total * FPS)} fps={FPS} width={1920} height={1080} />
  <Composition id="KaderB" component={KaderB} durationInFrames={Math.ceil(tB.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
