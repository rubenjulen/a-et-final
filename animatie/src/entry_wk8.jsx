import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { KaderE } from './KaderE';
import tE from './timing_kE.json';

const FPS = 30;
const Root = () => (<>
  <Composition id="KaderE" component={KaderE} durationInFrames={Math.ceil(tE.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
