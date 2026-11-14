import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { KaderD } from './KaderD';
import tD from './timing_kD.json';

const FPS = 30;
const Root = () => (<>
  <Composition id="KaderD" component={KaderD} durationInFrames={Math.ceil(tD.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
